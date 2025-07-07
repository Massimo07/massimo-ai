# massimo_ai_gen.py - UNIVERSAL PDF FIX - MASSIMO AI

import os
from docx import Document
from fpdf import FPDF
from deep_translator import GoogleTranslator

# LISTA LINGUE - TUTTE EUROPEE + RUSSO + CINESE + ARABO ecc.
LINGUE = {
    "it": "italiano",  "en": "english",    "fr": "francese",  "es": "spagnolo",   "de": "tedesco", "ru": "russo", "ar": "arabo", "zh": "cinese",
    "ro": "rumeno",    "pl": "polacco",    "sk": "slovacco",  "el": "greco",      "nl": "olandese", "pt": "portoghese", "sv": "svedese", "hu": "ungherese",
    "bg": "bulgaro",   "hr": "croato",     "cs": "ceco",      "da": "danese",     "et": "estone", "fi": "finlandese", "lv": "lettone", "lt": "lituano",
    "sl": "sloveno",   "sr": "serbo",      "mk": "macedone",  "sq": "albanese",   "ka": "georgiano", "mt": "maltese", "uk": "ucraino", "tr": "turco",
    "be": "bielorusso","bs": "bosniaco",   "no": "norvegese", "ga": "irlandese",  "ca": "catalano", "gl": "galiziano", "eu": "basco"
}

CORSI = [
    "network_marketing", "adobe_photoshop", "office", "excel", "canva", "telegram", "ai_assistant", "ai_copywriting", "ai_video", "video_editing",
    "automation", "autostima", "autotraining", "avatar_ai", "funnel", "gamification", "google_suite", "leadership", "mentalita_milionario",
    "notion", "personal_brand", "plugin_automazioni", "podcast", "podcast_radio", "presentazione_aziendale", "presentazione_piano_marketing",
    "presentazione_prodotti", "recruiting", "social_adv", "social", "tiktok", "time_management", "vendita", "vr_training", "webmaster", "web_design",
    "webinar", "youtube"
]

LIVELLI = 7
MODULI_PER_LIVELLO = 7

DESCRIZIONE = {
    "network_marketing": "Corso professionale di Network Marketing per Live On Plus, focalizzato sulla crescita della rete, recruiting, vendita, duplicazione, leadership, gestione team internazionale e formazione business.",
    "adobe_photoshop": "Corso completo Adobe Photoshop per networker e marketer: grafica, impaginazione, strumenti, creazione materiale promozionale, social e presentazioni professionali.",
    "office": "Office completo per network marketing: Word, Excel, PowerPoint, gestione documenti, presentazioni aziendali, report e automatismi.",
    "excel": "Corso Excel avanzato: database clienti, analisi fatturato, automatismi per team, analisi dati e presentazioni.",
    "canva": "Canva per il network marketing: grafica rapida, template social, presentazioni, materiale promo.",
    "telegram": "Telegram e WhatsApp per la gestione e crescita del team: automazioni, chat, broadcast, sicurezza.",
    "ai_assistant": "AI Assistant: come sfruttare l’intelligenza artificiale nella gestione team, recruiting, automazioni e formazione.",
    # ... Aggiungi intro per ogni corso ...
}

def genera_contenuto_modulo(corso, livello, modulo, lingua, descrizione_corso):
    testo = f"""\
{descrizione_corso}
\n
[Livello {livello} / Modulo {modulo} / Lingua: {LINGUE[lingua].capitalize()}]\n
Obiettivi didattici: Approfondimento totale – spiegazione dettagliata, grammatica (se serve), workflow reale per network marketing.\n
Teoria, pratica, dialoghi reali, esercizi pratici, quiz di verifica, errori comuni, best practice, vocabolario e cultura internazionale.
\n
(Contenuto esteso da generare qui via AI oppure a mano. Ogni modulo deve essere completo, professionale e spiegato come in un vero corso universitario, adattato al business LIVE ON PLUS / network marketing internazionale.)\n
---
"""
    return testo

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
    font_path = "DejaVuSans.ttf"  # Il font deve essere nella cartella dello script!
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

def traduci(testo, lingua_dest):
    if lingua_dest == "it":
        return testo
    try:
        return GoogleTranslator(source="auto", target=lingua_dest).translate(testo)
    except Exception:
        return testo

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
                    contenuto = genera_contenuto_modulo(corso, livello, modulo, lingua, descrizione_corso)
                    tradotto = traduci(contenuto, lingua)
                    nome_base = f"modulo{modulo}_{lingua}"
                    salva_txt(os.path.join(path_dir, f"{nome_base}.txt"), tradotto)
                    salva_md(os.path.join(path_dir, f"{nome_base}.md"), tradotto)
                    salva_docx(os.path.join(path_dir, f"{nome_base}.docx"), tradotto)
                    salva_pdf(os.path.join(path_dir, f"{nome_base}.pdf"), tradotto)
                    print(f"Creato: {corso}/L{livello}/M{modulo} [{lingua}]")

if __name__ == "__main__":
    main()
