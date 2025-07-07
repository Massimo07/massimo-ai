import os
from dotenv import load_dotenv
from elevenlabs import set_api_key, generate

# Carica variabili d'ambiente da .env
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
print(f"API key caricata: {api_key}")

if not api_key:
    raise ValueError("La variabile d'ambiente ELEVENLABS_API_KEY non è stata trovata")

set_api_key(api_key)

# Voce maschile naturale
voice = "Adam"   # Cambia in "Josh" se vuoi testare la differenza

# Correzioni di pronuncia personalizzate
correzioni = {
    "Michael": "Maicol",
    "Sarah": "Sèra",
    "Live On Plus": "Laiv On Plas",
    "WhatsApp": "Uozzapp",
    "Manuel": "Manuel",
    "Magic Team": "Mèggic Tim",
    "Diamond Black": "Daiamond Black"
}

def correggi_pronuncia(testo):
    for parola, pronuncia in correzioni.items():
        testo = testo.replace(parola, pronuncia)
    return testo

# INPUT UTENTE
testo_utente = input("Scrivi la frase che vuoi sentire (puoi usare parole miste):\n")
testo_corretto = correggi_pronuncia(testo_utente)

# GENERA AUDIO
audio_bytes = generate(text=testo_corretto, voice=voice)

# SALVA FILE
with open("output.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio generato (con correzione pronuncia) e salvato come output.wav")
