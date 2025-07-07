import os
import openai

# --- CONFIGURAZIONE OPENAI ---
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "INSERISCI-LA-TUA-KEY-QUI"
openai.api_key = OPENAI_API_KEY

# --- DATI DEL CORSO ---
CORSO = "Network Marketing"
LIVELLO = "Base"
LINGUA = "it"

def crea_contenuto_corso():
    prompt = f"""Crea un vero corso professionale, completo e dettagliato su '{CORSO}', livello {LIVELLO}, in lingua {LINGUA}.
- Il corso deve essere **strutturato** con: copertina (descritta a parole), indice dei moduli (almeno 8-12 titoli), spiegazione dettagliata per ogni modulo (non semplificare!), esercizi, checklist, quiz, box motivazionali, glossario, casi studio.
- Per ogni modulo indica un prompt per un'immagine AI business (NON generare immagini, solo il prompt).
- Lo stile dev'essere serio, tecnico, progressivo, educativo.
- Scrivi in formato markdown e dividi bene con titoli e sottotitoli.
Rispondi solo col corso, senza premesse, firma, né note aggiuntive.
"""
    messages = [
        {"role": "system", "content": "Sei un formatore esperto e impagini corsi aziendali per professionisti."},
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=4096,
        temperature=0.4
    )
    return response.choices[0].message.content

def main():
    print(f"Generazione: {CORSO} {LIVELLO} [{LINGUA}] ...")
    testo = crea_contenuto_corso()
    # Salva in file markdown
    outdir = "data/corsi"
    os.makedirs(outdir, exist_ok=True)
    filename = f"{outdir}/{CORSO.replace(' ','_').lower()}_{LIVELLO}_{LINGUA}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(testo)
    print(f"✅ Corso creato in: {filename}")

if __name__ == "__main__":
    main()
