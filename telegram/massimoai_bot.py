import os
import logging
import sqlite3
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import openai
from PyPDF2 import PdfReader

# === CONFIG ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "INSERISCI_LA_TUA_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "INSERISCI_LA_TUA_OPENAI_API_KEY")
DB_PATH = "massimoai_products.db"
PDF_FOLDER = "pdf"

logging.basicConfig(level=logging.INFO)
openai.api_key = OPENAI_API_KEY

def search_db(search):
    """Cerca nome, categoria, descrizione nel database prodotti."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name, price, description, url, image_url FROM products WHERE name LIKE ? OR description LIKE ?", (f"%{search}%", f"%{search}%"))
    results = cur.fetchall()
    conn.close()
    return results

def search_all_pdfs(search, folder=PDF_FOLDER):
    """Cerca testo in tutti i PDF, ritorna lista di (nome, path) con match."""
    results = []
    for fname in os.listdir(folder):
        if fname.lower().endswith(".pdf"):
            path = os.path.join(folder, fname)
            try:
                reader = PdfReader(path)
                fulltext = ""
                for page in reader.pages:
                    fulltext += page.extract_text() or ""
                if search.lower() in fulltext.lower():
                    results.append((fname, path))
            except Exception as e:
                logging.warning(f"Errore PDF {fname}: {e}")
    return results

def gpt4o_prompt(user_question, prodotti, pdf_found):
    """Crea il prompt 'AL MASSIMO' per GPT."""
    context = ""
    for prod in prodotti:
        context += f"\nPRODOTTO: {prod[0]}\nPREZZO: {prod[1]}\nDESC: {prod[2][:300]}...\nLINK: {prod[3]}\nIMMAGINE: {prod[4]}\n"
    for pdf in pdf_found:
        context += f"\nPDF PRESENTE: {pdf[0]}\n"
    prompt = f"""
Rispondi solo con dati certi, zero frasi generiche. Usa SOLO i dati qui sotto, come Massimo AI, esperto Live On Plus. Se hai PDF o prodotto, cita e allega.
DATI DISPONIBILI:
{context}
DOMANDA: {user_question}
Se non trovi info rispondi "Non trovato nei dati".
"""
    return prompt

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ciao! Sono Massimo AI (versione AL MASSIMO). Scrivi il nome di un prodotto, chiedimi un PDF o una domanda di marketing/networking. Ti risponderò solo usando i dati REALI del tuo sistema.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    domanda = update.message.text.strip()
    prodotti = search_db(domanda)
    pdfs = search_all_pdfs(domanda)
    prompt = gpt4o_prompt(domanda, prodotti, pdfs)
    try:
        completions = openai.chat.completions.create(
            model="gpt-4o",  # Cambia in "gpt-3.5-turbo" se non hai GPT-4o
            messages=[{"role": "system", "content": prompt}],
            temperature=0.2,
            max_tokens=600
        )
        answer = completions.choices[0].message.content.strip()
    except Exception as e:
        answer = f"Errore GPT: {e}"

    # Manda sempre la risposta AI
    await update.message.reply_text(answer)

    # Allegato: PDF se trovato
    for fname, path in pdfs:
        try:
            await update.message.reply_document(InputFile(path), caption=f"PDF rilevato: {fname}")
        except Exception as e:
            logging.warning(f"Errore invio PDF {fname}: {e}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("MASSIMO AI - BOT AL MASSIMO operativo! 🚀💎")
    app.run_polling()

if __name__ == "__main__":
    main()
