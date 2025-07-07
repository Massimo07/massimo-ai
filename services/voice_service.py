import os
from dotenv import load_dotenv
from elevenlabs import set_api_key, generate
from openai import OpenAI
from io import BytesIO

# Carica chiavi API dalle variabili d'ambiente (.env)
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not ELEVENLABS_API_KEY:
    raise Exception("API Key di ElevenLabs non trovata! Mettila nel file .env come ELEVENLABS_API_KEY")
if not OPENAI_API_KEY:
    raise Exception("API Key di OpenAI non trovata! Mettila nel file .env come OPENAI_API_KEY")

set_api_key(ELEVENLABS_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def stt(audio_bytes, lang="it"):
    """Trascrive audio (bytes) in testo usando OpenAI Whisper."""
    audio = BytesIO(audio_bytes)
    try:
        response = openai_client.audio.transcriptions.create(
            model="whisper-1",
            file=audio,
            language=lang
        )
        return response.text.strip()
    except Exception as e:
        return f"[STT error: {e}]"

def tts(text, lang="it", voice="Bella"):
    """Genera voce da testo con ElevenLabs e restituisce uno stream WAV."""
    try:
        audio_bytes = generate(text=text, voice=voice)
        return BytesIO(audio_bytes)
    except Exception as e:
        print(f"Errore generazione audio: {e}")
        return None

def ask_gpt(text, lang="it"):
    """Risponde come Massimo AI (GPT)."""
    system_prompt = (
        "Rispondi come Massimo AI. Tono professionale, motivazionale, concreto, diretto. "
        "Sintesi e valore pratico. Niente chiacchiere inutili."
    )
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[GPT error: {e}]"
