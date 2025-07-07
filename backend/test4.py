import os
import logging
from dotenv import load_dotenv
import openai
from elevenlabs import set_api_key, generate
import speech_recognition as sr

# Configurazione logging avanzata
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("MassimoAI")

# Carica variabili d'ambiente
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # Giorgio (modifica con quella che preferisci)

if not ELEVENLABS_API_KEY or not OPENAI_API_KEY:
    logger.error("API KEY mancanti: controlla il file .env.")
    exit(1)

set_api_key(ELEVENLABS_API_KEY)
openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chiedi_a_massimo_ai(testo_utente: str) -> str:
    """Invia una domanda a GPT-4o e restituisce la risposta concreta e professionale."""
    system_prompt = (
        "Rispondi come Massimo AI. Tono professionale, motivazionale, concreto, diretto. "
        "Sintesi e valore pratico. Niente chiacchiere inutili."
    )
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": testo_utente}
            ]
        )
        risposta_ai = response.choices[0].message.content.strip()
        logger.info("Risposta GPT-4o generata con successo.")
        return risposta_ai
    except Exception as e:
        logger.error(f"Errore durante chiamata OpenAI: {e}")
        return "Errore: impossibile ottenere risposta al momento."

def sintetizza_voce(testo: str, voice_id: str = VOICE_ID, output_file: str = "output.wav") -> bool:
    """Genera l'audio dalla risposta testuale e salva su file."""
    try:
        audio_bytes = generate(text=testo, voice=voice_id)
        with open(output_file, "wb") as f:
            f.write(audio_bytes)
        logger.info(f"Audio generato e salvato in {output_file}.")
        return True
    except Exception as e:
        logger.error(f"Errore generazione audio: {e}")
        return False

def ascolta_microfono():
    """Registra dal microfono finché non c'è silenzio (pausa di 1 secondo)."""
    r = sr.Recognizer()
    r.pause_threshold = 1.0  # 1 secondo di silenzio = fine frase
    with sr.Microphone() as source:
        print("\n🎤 Parla quando vuoi (pausa di 1s per finire)...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="it-IT")
        print("Hai detto:", text)
        return text
    except Exception as e:
        print("❌ Non ho capito, ripeti pure.")
        logger.error(f"Errore riconoscimento vocale: {e}")
        return None

def main():
    print("==== MASSIMO AI ADVANCED – MIC =====")
    while True:
        testo_utente = ascolta_microfono()
        if not testo_utente:
            continue
        risposta = chiedi_a_massimo_ai(testo_utente)
        print("\n===== RISPOSTA =====")
        print(risposta)
        print("====================\n")
        if sintetizza_voce(risposta):
            print("✔️ Audio pronto: output.wav")
        else:
            print("❌ Errore nella generazione dell'audio.")

if __name__ == "__main__":
    main()
