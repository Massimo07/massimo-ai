import os
from elevenlabs import set_api_key, generate

# Leggi la chiave API da variabile d'ambiente
api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    raise ValueError("La variabile d'ambiente ELEVENLABS_API_KEY non è stata trovata")

# Imposta la chiave API per ElevenLabs
set_api_key(api_key)

# Test di generazione audio
text = "Ciao, come va?"
voice = "Bella"

audio_bytes = generate(text=text, voice=voice)

# Salva su file
with open("output.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio generato e salvato come output.wav")
