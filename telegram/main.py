import os
import asyncio
import PyPDF2
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import openai

load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_KEY

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

user_states = {}

def lista_pdf_cartella(path="./data"):
    return [f for f in os.listdir(path) if f.lower().endswith(".pdf")]

def estrai_testo_pdf(percorso_pdf, max_pagine=12):
    testo = ""
    with open(percorso_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for i, page in enumerate(reader.pages):
            if i >= max_pagine:
                break
            page_text = page.extract_text()
            if page_text:
                testo += page_text
    return testo

async def get_ai_response(prompt):
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(
        None,
        lambda: openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Rispondi come un esperto Live On Plus, chiaro, concreto, aggiornato e motivazionale. Usa solo le informazioni affidabili del testo fornito."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )
    )
    return response.choices[0].message.content.strip()

# 19 voci definitive
menu_voci = [
    "🏢 Presentazione aziendale",
    "💎 Presentazione piano marketing",
    "🎯 Che vantaggi offre Live On Plus",
    "🌟 Perché scegliere il Magic Team",
    "📚 Cataloghi prodotti",
    "🧴 Ti consiglio il prodotto adatto a te",
    "❓ Domande Frequenti (FAQ)",
    "🆘 Hai bisogno di aiuto? Parliamone",
    "🛒 Vuoi fare vendita?",
    "🌐 Vuoi fare rete?",
    "🏷️ Vuoi fare autoconsumo?",
    "📖 Un libro per la tua crescita personale e professionale",
    "🏆 Testimonianze vere",
    "📞 Contatta il tuo sponsor",
    "🚀 Motivazione del giorno",
    "🎧 Radio M AI",
    "🔗 Invita un amico",
    "🪐 Entra nel futuro – Abbonati"
]

main_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=voce)] for voce in menu_voci],
    resize_keyboard=True
)
back_home = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🔙 Indietro"), KeyboardButton(text="🏠 Home")]],
    resize_keyboard=True
)

@dp.message(Command('start'))
async def start(msg: types.Message):
    user_states[msg.chat.id] = None
    await msg.answer(
        "Ciao! Benvenuto/a in Massimo AI. Come ti chiami?",
        reply_markup=types.ReplyKeyboardRemove()
    )

# Nome utente: mostra menu principale
@dp.message(lambda m: m.text not in menu_voci + ["🔙 Indietro", "🏠 Home"] and not (m.text and m.text.endswith(".pdf")) and not (m.text and (m.text.startswith("📄 Scarica ") or m.text.startswith("🧠 Spiegami una parte di "))))
async def nome_utente(msg: types.Message):
    user_name = msg.text.strip()
    await msg.answer(
        f"Perfetto, {user_name}! Ecco il menu Massimo AI:",
        reply_markup=main_menu
    )

@dp.message(lambda m: m.text == "🏠 Home" or m.text == "🔙 Indietro")
async def home(msg: types.Message):
    user_states[msg.chat.id] = None
    await msg.answer("Menu principale:", reply_markup=main_menu)

# 1. Presentazione aziendale (risposta AI o da PDF)
@dp.message(lambda m: m.text == "🏢 Presentazione aziendale")
async def presentazione_azienda(msg: types.Message):
    pdfs = lista_pdf_cartella()
    pdf_presentazione = None
    for f in pdfs:
        if "presentazione" in f.lower() or "piano compensi" in f.lower():
            pdf_presentazione = f
            break
    if pdf_presentazione:
        testo_pdf = estrai_testo_pdf(f"./data/{pdf_presentazione}", max_pagine=6)
        prompt = (
            "Presenta l’azienda Live On Plus in modo chiaro, ispirazionale e fedele, "
            "usando solo dati e valori reali da questa presentazione ufficiale:\n" + testo_pdf[:4000]
        )
        risposta = await get_ai_response(prompt)
        await msg.answer(risposta, reply_markup=back_home)
    else:
        await msg.answer("PDF di presentazione azienda non trovato in /data.", reply_markup=back_home)

# 2. Presentazione piano marketing
@dp.message(lambda m: m.text == "💎 Presentazione piano marketing")
async def presentazione_marketing(msg: types.Message):
    pdfs = lista_pdf_cartella()
    pdf_marketing = None
    for f in pdfs:
        if "compensi" in f.lower() or "marketing" in f.lower():
            pdf_marketing = f
            break
    if pdf_marketing:
        testo_pdf = estrai_testo_pdf(f"./data/{pdf_marketing}", max_pagine=12)
        prompt = (
            "Spiega il piano marketing Live On Plus in modo semplice e motivante, "
            "usando solo info del PDF seguente:\n" + testo_pdf[:4000]
        )
        risposta = await get_ai_response(prompt)
        await msg.answer(risposta, reply_markup=back_home)
    else:
        await msg.answer("PDF del piano marketing non trovato in /data.", reply_markup=back_home)

# 3. Vantaggi Live On Plus
@dp.message(lambda m: m.text == "CHE VANTAGGI OFFRE LIVE ON PLUS")
async def vantaggi_liveonplus(msg: types.Message):
    risposta = await get_ai_response(
        "Elenca tutti i vantaggi concreti e motivanti che Live On Plus offre ai suoi iscritti e collaboratori, sia dal punto di vista economico che personale. Fai risaltare i punti di forza rispetto alla concorrenza."
    )
    await msg.answer(risposta, reply_markup=back_home)

# 4. Perché scegliere il Magic Team
@dp.message(lambda m: m.text == "🌟 Perché scegliere il Magic Team")
async def perche_magic_team(msg: types.Message):
    risposta = await get_ai_response(
        "Spiega in modo empatico e coinvolgente perché una persona dovrebbe scegliere il Magic Team, quali sono i valori, il supporto e la differenza rispetto agli altri team."
    )
    await msg.answer(risposta, reply_markup=back_home)

# 5. Cataloghi prodotti: menu automatico PDF
@dp.message(lambda m: m.text == "📚 Cataloghi prodotti")
async def cataloghi_pdf(msg: types.Message):
    pdf_files = lista_pdf_cartella()
    if not pdf_files:
        await msg.answer("Non ci sono PDF nella cartella /data. Aggiungili e riprova.", reply_markup=back_home)
        return
    menu_cataloghi = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=nome)] for nome in pdf_files] +
                 [[KeyboardButton(text="🔙 Indietro"), KeyboardButton(text="🏠 Home")]],
        resize_keyboard=True
    )
    await msg.answer(
        "Seleziona il PDF che vuoi scaricare o su cui vuoi ricevere una spiegazione:",
        reply_markup=menu_cataloghi
    )

# Handler per ogni PDF
@dp.message(lambda m: m.text and m.text.endswith(".pdf"))
async def gestisci_catalogo_pdf(msg: types.Message):
    nome_pdf = msg.text
    user_states[msg.chat.id] = f"attesa_scelta_{nome_pdf}"
    await msg.answer(
        f"Hai selezionato **{nome_pdf}**.\nVuoi scaricare il PDF completo o ricevere una spiegazione AI su una parte specifica?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=f"📄 Scarica {nome_pdf}")],
                [KeyboardButton(text=f"🧠 Spiegami una parte di {nome_pdf}")],
                [KeyboardButton(text="🔙 Indietro"), KeyboardButton(text="🏠 Home")]
            ],
            resize_keyboard=True
        )
    )

@dp.message(lambda m: m.text and m.text.startswith("📄 Scarica "))
async def scarica_qualunque_pdf(msg: types.Message):
    nome_pdf = msg.text.replace("📄 Scarica ", "")
    user_states[msg.chat.id] = None
    try:
        await msg.answer_document(
            open(f"./data/{nome_pdf}", "rb"),
            caption=f"Ecco il PDF {nome_pdf}",
            reply_markup=back_home
        )
    except Exception as e:
        await msg.answer("Non trovo questo PDF nella cartella /data.", reply_markup=back_home)

@dp.message(lambda m: m.text and m.text.startswith("🧠 Spiegami una parte di "))
async def chiedi_parte_qualunque_pdf(msg: types.Message):
    nome_pdf = msg.text.replace("🧠 Spiegami una parte di ", "")
    user_states[msg.chat.id] = f"attesa_spiegazione_{nome_pdf}"
    await msg.answer(
        f"Scrivi la parte che vuoi approfondire di **{nome_pdf}** (es: bonus, ingredienti, utilizzo, regole, prodotti, ecc.)"
    )

# 6. Consiglio prodotto
@dp.message(lambda m: m.text == "🧴 Ti consiglio il prodotto adatto a te")
async def consiglio_prodotto(msg: types.Message):
    user_states[msg.chat.id] = "attesa_prodotto"
    await msg.answer(
        "Scrivi qui sotto che tipo di esigenza hai (es: pelle sensibile, capelli ricci, un profumo che dura a lungo, ecc.) e ti consiglierò il prodotto più adatto!"
    )

# 7. FAQ
@dp.message(lambda m: m.text == "❓ Domande Frequenti (FAQ)")
async def faq(msg: types.Message):
    user_states[msg.chat.id] = "attesa_faq"
    await msg.answer("Fai qualsiasi domanda su Live On Plus, network marketing o prodotti e ti risponderò subito!")

# 8. Supporto emotivo
@dp.message(lambda m: m.text == "🙋‍♂️ Hai bisogno di aiuto? PARLIAMONE")
async def supporto_emotivo(msg: types.Message):
    user_states[msg.chat.id] = "attesa_supporto"
    await msg.answer(
        "Raccontami cosa ti preoccupa, cosa senti o quale difficoltà hai (anche fuori dal network). Massimo AI è qui per ascoltarti e aiutarti con empatia e risposte umane."
    )

# 9. 10. 11. – Placeholder (personalizza per iscrizione/rete/autoconsumo)
@dp.message(lambda m: m.text in ["🛒 Vuoi fare vendita?", "🌐 Vuoi fare rete?", "🏷 Vuoi fare autoconsumo?"])
async def vendita_rete_autoconsumo(msg: types.Message):
    await msg.answer("Funzione iscrizione e scelta sponsor disponibile nella versione avanzata.", reply_markup=back_home)

# 12. Libro crescita personale
@dp.message(lambda m: m.text == "📖 Un libro per la tua crescita personale e professionale")
async def libro_crescita(msg: types.Message):
    await msg.answer("Per la tua crescita personale ti consiglio questo libro fondamentale: [Scopri e acquista su Amazon](https://www.amazon.it/tuo-libro-link).", reply_markup=back_home)

# 13. Testimonianze vere
@dp.message(lambda m: m.text == "🔑 🏆 Testimonianze vere")
async def testimonianze(msg: types.Message):
    await msg.answer("Leggi le testimonianze vere sulla pagina ufficiale: [Testimonianze su Facebook](https://www.facebook.com/liveonplus/testimonianze)", reply_markup=back_home)

# 14. Contatta sponsor
@dp.message(lambda m: m.text == "📞 Contatta il tuo sponsor")
async def contatta_sponsor(msg: types.Message):
    await msg.answer("Funzione contatto sponsor disponibile nella versione avanzata.", reply_markup=back_home)

# 15. Motivazione del giorno (AI)
@dp.message(lambda m: m.text == "🚀 Motivazione del giorno")
async def motivazione_giorno(msg: types.Message):
    risposta = await get_ai_response(
        "Genera una frase motivazionale per chi inizia il percorso Live On Plus, breve, potente, adatta a chi ha bisogno di energia e fiducia oggi."
    )
    await msg.answer(risposta, reply_markup=back_home)

# 16. Radio M AI (placeholder)
@dp.message(lambda m: m.text == "🎧 Radio M AI")
async def radio_ai(msg: types.Message):
    await msg.answer("Funzione in sviluppo: presto potrai ascoltare Radio M AI direttamente qui!", reply_markup=back_home)

# 17. Cambia lingua (placeholder)
@dp.message(lambda m: m.text == "🔄 Cambia lingua")
async def cambia_lingua(msg: types.Message):
    await msg.answer("Massimo AI è disponibile solo in italiano. Le altre lingue arriveranno presto!", reply_markup=back_home)

# 18. Invita un amico
@dp.message(lambda m: m.text == "🔗 Invita un amico")
async def invita_amico(msg: types.Message):
    await msg.answer(
        "Invita un amico con il tuo referral link! Può scegliere se diventare venditore, far parte della rete o fare autoconsumo. Tutte le registrazioni saranno collegate al tuo profilo.",
        reply_markup=back_home
    )

# 19. Entra nel futuro
@dp.message(lambda m: m.text == "E ORA… PREPARATI… SI ENTRA NEL FUTURO")
async def entra_nel_futuro(msg: types.Message):
    await msg.answer(
        "Scopri i 7 livelli di Massimo AI: dal primo passo fino al Black Diamond! Ogni livello offre corsi, servizi e strumenti esclusivi. Scegli l’abbonamento che vuoi sbloccare per accelerare la tua crescita. (Funzione in sviluppo, disponibile a breve!)",
        reply_markup=back_home
    )

# Handler AI generico per risposte a richieste “attesa_prodotto”, “attesa_faq”, “attesa_supporto” e ogni PDF
@dp.message()
async def ai_risposta_generica(msg: types.Message):
    stato = user_states.get(msg.chat.id, None)
    if stato and stato.startswith("attesa_spiegazione_"):
        nome_pdf = stato.replace("attesa_spiegazione_", "")
        percorso_pdf = f"./data/{nome_pdf}"
        if not os.path.isfile(percorso_pdf):
            await msg.answer("Il PDF non esiste più. Torna al menu principale.", reply_markup=main_menu)
            user_states[msg.chat.id] = None
            return
        testo_pdf = estrai_testo_pdf(percorso_pdf, max_pagine=12)
        prompt = (
            f"Rispondi in modo chiaro e dettagliato usando solo informazioni dal PDF '{nome_pdf}'. "
            f"L'utente chiede: '{msg.text}'.\n\n"
            f"Ecco il testo ufficiale:\n\n{testo_pdf[:4000]}"
        )
        risposta = await get_ai_response(prompt)
        await msg.answer(risposta, reply_markup=back_home)
        user_states[msg.chat.id] = None
    elif stato == "attesa_prodotto":
        risposta = await get_ai_response(
            f"Consiglia uno o più prodotti Live On Plus a chi ha questa esigenza: {msg.text}. Motiva la scelta come un esperto consulente."
        )
        await msg.answer(risposta, reply_markup=back_home)
        user_states[msg.chat.id] = None
    elif stato == "attesa_faq":
        risposta = await get_ai_response(
            f"Rispondi a questa domanda come un esperto di network marketing Live On Plus: {msg.text}"
        )
        await msg.answer(risposta, reply_markup=back_home)
        user_states[msg.chat.id] = None
    elif stato == "attesa_supporto":
        risposta = await get_ai_response(
            f"Rispondi come un coach empatico e motivazionale a questa richiesta di supporto personale: {msg.text}"
        )
        await msg.answer(risposta, reply_markup=back_home)
        user_states[msg.chat.id] = None

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())