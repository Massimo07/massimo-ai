import os
import openai
from dotenv import load_dotenv
from datetime import datetime
import requests

# Carica API Key da .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Lista lingue, corsi e livelli (ridotta per esempio)
lingue = [("it", "Italiano"), ("en", "Inglese")]
livelli = ["livello1", "livello2"]

corsi_tecnici = ["adobe"]
indici_corsi = {
    "adobe": [
        "Introduzione ad Adobe per il Network Marketing",
        "Adobe Photoshop: basi e applicazioni"
    ]
}

def genera_modulo_gpt(nome_modulo, corso, livello, lingua_dest):
    prompt = f"""
Sviluppa in modo dettagliato il modulo '{nome_modulo}' del corso '{corso}', livello '{livello}', in lingua '{lingua_dest}'.
Scrivi spiegazioni, esempi, esercizi, quiz, glossario, checklist e un caso studio.
Almeno 45 righe (1 pagina A4).
"""
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response.choices[0].message.content

def genera_immagine_ai(descrizione, save_path):
    response = openai.image.create(
        prompt=descrizione,
        n=1,
        size="1024x1024"
    )
    url_immagine = response['data'][0]['url']
    img_data = requests.get(url_immagine).content
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'wb') as f:
        f.write(img_data)
    print(f"Immagine salvata: {save_path}")

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
                fout.write(fin.read() + "\n\n" + ("-"*40) + "\n\n")

if __name__ == "__main__":
    today = datetime.now().strftime('%Y-%m-%d')
    for codice, lingua_nome in lingue:
        for corso in corsi_tecnici:
            for livello in livelli:
                moduli = indici_corsi.get(corso, [])
                base_dir = os.path.join("massimo_ai", "data", "corsi", codice, corso)
                corso_folder = os.path.join(base_dir, f"{livello}_{today}")
                immagini_folder = os.path.join(corso_folder, "immagini")
                print(f"\n=== Generazione corso {corso} – {livello} – {lingua_nome} ===")

                for idx, modulo_nome in enumerate(moduli):
                    print(f"Modulo {idx+1}: {modulo_nome}")
                    testo_modulo = genera_modulo_gpt(modulo_nome, corso, livello, lingua_nome)
                    salva_modulo(corso_folder, idx, modulo_nome, testo_modulo)

                    # Genera immagine per modulo (descrizione sintetica)
                    descrizione_immagine = f"Grafica professionale per '{modulo_nome}', stile moderno per network marketing"
                    img_path = os.path.join(immagini_folder, f"{idx+1:02d}_{modulo_nome.replace(' ','_')}.png")
                    genera_immagine_ai(descrizione_immagine, img_path)

                file_finale = os.path.join(corso_folder, f"{corso}_{livello}_{lingua_nome}_completo.txt")
                unisci_moduli(corso_folder, file_finale)
                print(f"✅ Corso completo generato: {file_finale}")
