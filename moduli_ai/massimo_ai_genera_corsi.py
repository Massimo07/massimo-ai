import os
import openai
from dotenv import load_dotenv
from datetime import datetime
from itertools import product

# Carica la API Key da .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Lista completa lingue ufficiali europee + russo, cinese, arabo (codice ISO, nome)
lingue = [
    ("it", "Italiano"), ("en", "Inglese"), ("fr", "Francese"),
    ("de", "Tedesco"), ("es", "Spagnolo"), ("pt", "Portoghese"),
    ("nl", "Olandese"), ("el", "Greco"), ("ro", "Rumeno"), ("hu", "Ungherese"),
    ("pl", "Polacco"), ("cs", "Ceco"), ("sk", "Slovacco"), ("bg", "Bulgaro"),
    ("hr", "Croato"), ("sl", "Sloveno"), ("sv", "Svedese"), ("da", "Danese"),
    ("fi", "Finlandese"), ("et", "Estone"), ("lv", "Lettone"), ("lt", "Lituano"),
    ("no", "Norvegese"), ("ga", "Irlandese"), ("mt", "Maltese"), ("sq", "Albanese"),
    ("sr", "Serbo"), ("bs", "Bosniaco"), ("me", "Montenegrino"), ("mk", "Macedone"),
    ("tr", "Turco"), ("uk", "Ucraino"), ("be", "Bielorusso"), ("ka", "Georgiano"),
    ("hy", "Armeno"), ("rm", "Rumantsch"), ("lb", "Lussemburghese"),
    ("is", "Islandese"), ("ca", "Catalano"),
    ("ru", "Russo"), ("zh", "Cinese"), ("ar", "Arabo")
]

# Livelli corso
livelli = ["livello1", "livello2", "livello3", "livello4", "livello5", "livello6", "livello7"]

# 37 corsi professionali
corsi_tecnici = [
    "adobe", "office", "ai_assistant", "ai_copywriting", "copywriting",
    "ai_video", "video_editing", "automation", "autostima", "autotraining",
    "avatar_ai", "canva", "funnel", "gamification", "google_suite",
    "leadership", "mentalita_milionario", "network_marketing", "notion",
    "personal_brand", "plugin_automazioni", "podcast", "podcast_radio",
    "presentazione_aziendale", "presentazione_piano_marketing",
    "presentazione_prodotti", "recruiting", "social_adv", "social",
    "tiktok", "time_management", "vendita", "vr_training", "web_master",
    "web_design", "webinar", "youtube"
]

# Indici moduli (esempio base per tutti i corsi, da personalizzare/modificare per ciascuno)
indici_corsi = {corso: [
    f"Modulo {i+1} - Argomento importante del corso {corso}" for i in range(10)
] for corso in corsi_tecnici}

def genera_modulo_gpt(nome_modulo, corso, livello, lingua_src, lingua_dest, tipo_corso="professionale"):
    """
    Genera il testo di un modulo usando GPT.
    tipo_corso: 'professionale' o 'lingua'
    Per corsi di lingua, lingua_src è la lingua di partenza e lingua_dest quella da imparare.
    """
    if tipo_corso == "professionale":
        prompt = f"""
Sviluppa in modo completo e dettagliato il modulo '{nome_modulo}' del corso '{corso}', livello '{livello}', in lingua '{lingua_dest}'.
Scrivi spiegazioni approfondite, esempi pratici, esercizi, quiz, glossario specifico, checklist, box motivazione e un caso studio reale.
La lunghezza deve essere almeno 1 pagina A4 (circa 45 righe, font 11).
Non limitarti a titoli o riassunti, sviluppa ogni concetto da vero formatore accademico.
"""
    else:
        prompt = f"""
Crea un modulo di corso di lingua per imparare '{lingua_dest}' partendo da '{lingua_src}', livello '{livello}'.
Ogni frase deve essere spiegata in italiano (o lingua sorgente), seguita dalla traduzione nella lingua target e dalla pronuncia semplificata.
Inserisci dialoghi reali, esercizi pratici, quiz, glossari e contenuti utili per un professionista del network marketing.
La lunghezza minima è 1 pagina A4 (circa 45 righe, font 11).
"""

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response.choices[0].message.content

def salva_modulo(cartella, idx, nome_modulo, testo):
    os.makedirs(cartella, exist_ok=True)
    safe_nome = nome_modulo.replace(" ", "_")[:40]
    filename = f"{idx+1:02d}_{safe_nome}.txt"
    with open(os.path.join(cartella, filename), "w", encoding="utf-8") as f:
        f.write(testo)

def unisci_moduli(cartella, out_file):
    files = sorted([f for f in os.listdir(cartella) if f.endswith('.txt')])
    with open(out_file, "w", encoding="utf-8") as fout:
        for f in files:
            with open(os.path.join(cartella, f), "r", encoding="utf-8") as fin:
                fout.write(fin.read() + "\n\n" + ("-"*60) + "\n\n")

def genera_corsi_professionali():
    today = datetime.now().strftime('%Y-%m-%d')
    for codice, lingua_nome in lingue:
        for corso in corsi_tecnici:
            for livello in livelli:
                moduli = indici_corsi.get(corso, [])
                if not moduli:
                    print(f"[WARNING] Nessun indice moduli per corso: {corso}")
                    continue
                base_dir = os.path.join("massimo_ai", "data", "corsi", codice, corso)
                corso_folder = os.path.join(base_dir, f"{livello}_{today}")
                print(f"\n=== Generazione corso PROFESSIONALE {corso} – {livello} – {lingua_nome} ===")

                for idx, modulo_nome in enumerate(moduli):
                    print(f"Modulo {idx+1}: {modulo_nome}")
                    testo_modulo = genera_modulo_gpt(modulo_nome, corso, livello, lingua_nome, lingua_nome, tipo_corso="professionale")
                    salva_modulo(corso_folder, idx, modulo_nome, testo_modulo)

                file_finale = os.path.join(corso_folder, f"{corso}_{livello}_{lingua_nome}_completo.txt")
                unisci_moduli(corso_folder, file_finale)
                print(f"✅ Corso professionale completato: {file_finale}")

def genera_corsi_lingue():
    today = datetime.now().strftime('%Y-%m-%d')
    for lingua_src_code, lingua_src_nome in lingue:
        for lingua_dest_code, lingua_dest_nome in lingue:
            if lingua_src_code == lingua_dest_code:
                continue
            for livello in livelli:
                corso_folder = os.path.join("massimo_ai", "data", "corsi_lingue", f"{lingua_src_code}_{lingua_dest_code}", f"{livello}_{today}")
                modulo_nome = f"Corso lingua {lingua_dest_nome} da {lingua_src_nome} - {livello}"
                print(f"\n=== Generazione corso LINGUA {lingua_src_nome} -> {lingua_dest_nome} – {livello} ===")

                testo_modulo = genera_modulo_gpt(modulo_nome, "corso_lingua", livello, lingua_src_nome, lingua_dest_nome, tipo_corso="lingua")
                salva_modulo(corso_folder, 0, modulo_nome, testo_modulo)

                file_finale = os.path.join(corso_folder, f"corso_lingua_{lingua_src_code}_{lingua_dest_code}_{livello}_completo.txt")
                unisci_moduli(corso_folder, file_finale)
                print(f"✅ Corso lingua completato: {file_finale}")

if __name__ == "__main__":
    print("### Avvio generazione corsi professionali ###")
    genera_corsi_professionali()

    print("\n### Avvio generazione corsi di lingua NxN ###")
    genera_corsi_lingue()
