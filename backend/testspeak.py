import os
from dotenv import load_dotenv
import openai
from elevenlabs import set_api_key, generate
import sounddevice as sd
import numpy as np
import wavio
import speech_recognition as sr

# --- CARICA LE VARIABILI D'AMBIENTE DAL FILE .env ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY non trovata nel .env")
if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY non trovata nel .env")

openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)
set_api_key(ELEVENLABS_API_KEY)

DURATION = 6  # secondi di registrazione
FS = 44100    # frequenza di campionamento

def record_audio(filename="input.wav"):
    print("Parla ora...")
    audio = sd.rec(int(DURATION * FS), samplerate=FS, channels=1, dtype='int16')
    sd.wait()
    wavio.write(filename, audio, FS, sampwidth=2)
    print("Registrazione terminata.")
    return filename

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language="it-IT")
    print(f"Hai detto: {text}")
    return text

def ask_gpt(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4o",  # usa anche "gpt-4-1106-preview" se non hai accesso a 4o
        messages=[
            {"role": "system", "content": "Rispondi in modo amichevole, umano, empatico come Massimo AI, voce maschile, chiara, naturale. Rispondi sempre in italiano."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def speak(text, voice="Adam"):
    correzioni = {
        "Michael": "Maicol",
        "Sarah": "Sèra",
        "Live On Plus": "Laiv On Plas",
        "WhatsApp": "Uozzapp",
        "Manuel": "Manuel",
        "Magic Team": "Mèggic Tim",
        "Diamond Black": "Daiamond Black"
    }
    for k, v in correzioni.items():
        text = text.replace(k, v)
    audio_bytes = generate(text=text, voice=voice)
    out_file = "output.wav"
    with open(out_file, "wb") as f:
        f.write(audio_bytes)
    # riproduci l'audio (Windows)
    try:
        import simpleaudio as sa
        wave_obj = sa.WaveObject.from_wave_file(out_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print(f"Audio salvato in {out_file}, riproduzione fallita: {e}")

if __name__ == "__main__":
    # 1. REGISTRA AUDIO
    audio_file = record_audio()
    # 2. CONVERTI IN TESTO
    testo = speech_to_text(audio_file)
    # 3. CHAT CON GPT-4
    risposta = ask_gpt(testo)
    print(f"Massimo AI: {risposta}")
    # 4. SINTESI VOCALE
    speak(risposta, voice="Adam")
