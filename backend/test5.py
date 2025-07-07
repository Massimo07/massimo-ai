import os
import logging
from dotenv import load_dotenv
import openai
from elevenlabs import set_api_key, generate
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

# Config log
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("MassimoAI")

# Carica chiavi API
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # Giorgio, cambia se vuoi

if not ELEVENLABS_API_KEY or not OPENAI_API_KEY:
    logger.error("API KEY mancanti: controlla il file .env.")
    exit(1)

set_api_key(ELEVENLABS_API_KEY)
openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

def ascolta_microfono():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Parla ora (quando finisci resta in silenzio per 1-2 secondi)...")
        audio = r.listen(source)
    try:
        testo = r.recognize_google(audio, language="it-IT")
        logger.info(f"Hai detto: {testo}")
        return testo
    except sr.UnknownValueError:
        logger.warning("Non ho capito, ripeti pure.")
        return None

def chiedi_a_massimo_ai(testo_utente: str) -> str:
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

def sintetizza_voce(testo: str, voice_id: str = VOICE_ID):
    try:
        audio_bytes = generate(text=testo, voice=voice_id)
        logger.info("Audio generato.")
        return BytesIO(audio_bytes)
    except Exception as e:
        logger.error(f"Errore generazione audio: {e}")
        return None

def riproduci_audio(audio_stream):
    try:
        sound = AudioSegment.from_file(audio_stream, format="wav")
        play(sound)
        logger.info("Audio riprodotto.")
    except Exception as e:
        logger.error(f"Errore nella riproduzione audio: {e}")

def main():
    print("==== MASSIMO AI ADVANCED – MIC ====")
    while True:
        testo_utente = ascolta_microfono()
        if not testo_utente:
            continue
        if testo_utente.lower() in ["esci", "exit", "stop"]:
            print("Chiusura Massimo AI.")
            break
        risposta = chiedi_a_massimo_ai(testo_utente)
        print("\n===== RISPOSTA =====")
        print(risposta)
        print("====================\n")
        audio_stream = sintetizza_voce(risposta)
        if audio_stream:
            riproduci_audio(audio_stream)
        else:
            print("❌ Errore nella generazione o riproduzione dell'audio.")

if __name__ == "__main__":
    main()
