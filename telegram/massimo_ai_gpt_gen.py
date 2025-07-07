import os
import openai
from dotenv import load_dotenv
from docx import Document
from fpdf import FPDF
from deep_translator import GoogleTranslator

# Carica variabili d'ambiente dal file .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# LISTA LINGUE
LINGUE = {
    "it": "italiano",  "en": "english",    "fr": "francese",  "es": "spagnolo",   "de": "tedesco", "ru": "russo", "ar": "arabo", "zh": "cinese",
    "ro": "rumeno",    "pl": "polacco",    "sk": "slovacco",  "el": "greco",      "nl": "olandese", "pt": "portoghese", "sv": "svedese", "hu": "ungherese",
    "bg": "bulgaro",   "hr": "croato",     "cs": "ceco",      "da": "danese",     "et": "estone", "fi": "finlandese", "lv": "lettone", "lt": "lituano",
    "sl": "sloveno",   "sr": "serbo",      "mk": "macedone",  "sq": "albanese",   "ka": "georgiano", "mt": "maltese", "uk": "ucraino", "tr": "turco",
    "be": "bielorusso","bs": "bosniaco",   "no": "norvegese", "ga": "irlandese",  "ca": "catalano", "gl": "galiziano", "eu": "basco"
}

# ESEMPI CORSI
CORSI = [
    "network_marketing", "adobe_photoshop", "office", "excel", "canva", "telegram", "ai_assistant", "ai_copywriting", "ai_video", "video_editing",
    "automation", "autostima", "autotraining", "avatar_ai", "funnel", "gamification", "google_suite", "leadership", "mentalita_milionario",
    "notion", "personal_brand", "plugin_automazioni", "podcast", "podcast_radio", "presentazione_aziendale", "presentazione_piano_marketing",
    "presentazione_prodotti", "recruiting", "social_adv", "social", "tiktok", "time_management", "vendita", "vr_training", "webmaster", "web_design",
    "webinar", "youtube"
]

# PER TEST lascia LIVELLI e MODULI bassi, poi aumenta
LIVELLI = 2
MODULI_PER_LIVELLO = 1

DESCRIZIONE = {
    "network_marketing": "Corso professionale di Network Marketing per Live On Plus, focalizzato su crescita rete, recruiting, vendita, duplicazione, leadership e gestione team internazionale.",
    # ... aggiungi intro per ogni corso ...
}

def prompt_gpt(corso, livello, modulo, lingua, descrizione_corso):
    lingua_nome = LINGUE[lingua].capitalize()
    prompt = f"""
Sei un docente professionale di network marketing e business digitale. Crea un modulo didattico COMPLETO E DETTAGLIATO per il corso "{descrizione_corso}" (corso: {corso}, livello {livello}, modulo {modulo}), in lingua {lingua_nome}.

Il modulo deve includere:
- Spiegazione approfondita di teoria e pratica
- Esempi reali adattati al network marketing e Live On Plus
- Esercizi e quiz con soluzioni
- Dialoghi reali per WhatsApp, Telegram, Zoom, email
- Errori comuni e come evitarli
- Approfondimenti di cultura business internazionale
- Tutto spiegato passo-passo come se l'utente fosse un principiante assoluto, ma con linguaggio professionale.
- La lunghezza deve essere almeno 800 parole

NON scrivere punti elenco vuoti o titoli senza testo, solo contenuto vero, didattico e spiegato.

Scrivi in lingua {lingua_nome.upper()}.
"""
    return prompt

def genera_contenuto_modulo(corso, livello, modulo, lingua, descrizione_corso):
    prompt = prompt_gpt(corso, livello, modulo, lingua, descrizione_corso)
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Sei un docente universitario. Scrivi come a un principiante, con spiegazioni ultra dettagliate, step by step."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=3900
    )
    return response.choices[0].message.content

def salva_txt(path, contenuto):
    with open(path, "w", encoding="utf-8") as f:
        f.write(contenuto)

def salva_md(path, contenuto):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# " + contenuto)

def salva_docx(path, contenuto):
    doc = Document()
    for line in contenuto.split('\n'):
        doc.add_paragraph(line)
    doc.save(path)

def salva_pdf(path, contenuto):
    font_path = "DejaVuSans.ttf"
    if not os.path.isfile(font_path):
        raise Exception("Scarica 'DejaVuSans.ttf' (https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/DejaVuSans.ttf) e mettilo nella cartella dello script!")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.set_font('DejaVu', '', 11)
    for line in contenuto.split('\n'):
        pdf.multi_cell(0, 8, line)
    pdf.output(path)

def main():
    base_dir = "data_massimo_ai"
    os.makedirs(base_dir, exist_ok=True)
    for corso in CORSI:
        descrizione_corso = DESCRIZIONE.get(corso, corso.replace("_", " ").capitalize())
        for livello in range(1, LIVELLI+1):
            for modulo in range(1, MODULI_PER_LIVELLO+1):
                for lingua in LINGUE:
                    path_dir = os.path.join(base_dir, corso, f"livello{livello}")
                    os.makedirs(path_dir, exist_ok=True)
                    print(f"Generazione: {corso}/L{livello}/M{modulo} [{lingua}] ...")
                    contenuto = genera_contenuto_modulo(corso, livello, modulo, lingua, descrizione_corso)
                    nome_base = f"modulo{modulo}_{lingua}"
                    salva_txt(os.path.join(path_dir, f"{nome_base}.txt"), contenuto)
                    salva_md(os.path.join(path_dir, f"{nome_base}.md"), contenuto)
                    salva_docx(os.path.join(path_dir, f"{nome_base}.docx"), contenuto)
                    salva_pdf(os.path.join(path_dir, f"{nome_base}.pdf"), contenuto)
    print("\n✅ GENERAZIONE COMPLETATA! Tutto pronto in data_massimo_ai/")

if __name__ == "__main__":
    main()
