import os
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import openai
from elevenlabs import set_api_key, generate
from dotenv import load_dotenv

# Carica variabili da .env (deve essere nella stessa cartella)
load_dotenv()

# Imposta le API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
set_api_key(ELEVENLABS_API_KEY)
openai.api_key = OPENAI_API_KEY

# Parametri di registrazione
SAMPLERATE = 16000
DURATION = 7  # secondi, puoi aumentare

def registra_audio(filename="registrazione.wav"):
    print("Premi invio e parla...")
    input()
    print("Registrazione in corso...")
    audio = sd.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=1)
    sd.wait()
    sf.write(filename, audio, SAMPLERATE)
    print("Registrazione terminata.")
    return filename

def riconosci_audio(filename="registrazione.wav"):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    try:
        testo = r.recognize_google(audio, language="it-IT")
        print(f"Hai detto: {testo}")
        return testo
    except Exception as e:
        print("Errore riconoscimento vocale:", e)
        return ""

def ask_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Sei Massimo AI, assistente motivazionale e network marketing."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def parla_con_elevenlabs(text, voice="Adam"):
    audio_bytes = generate(text=text, voice=voice)
    with open("output.wav", "wb") as f:
        f.write(audio_bytes)
    print("Risposta salvata in output.wav")
    # Riproduzione audio
    try:
        import simpleaudio as sa
        wave_obj = sa.WaveObject.from_wave_file("output.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print("Errore riproduzione audio:", e)

if __name__ == "__main__":
    while True:
        filename = registra_audio()
        testo_utente = riconosci_audio(filename)
        if testo_utente:
            risposta = ask_gpt(testo_utente)
            print(f"Massimo AI: {risposta}")
            parla_con_elevenlabs(risposta)
        else:
            print("Non ho capito. Vuoi riprovare? [Invio per continuare, q per uscire]")
            if input().strip().lower() == 'q':
                break
