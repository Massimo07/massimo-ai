import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse
from elevenlabs.simple import generate, save, set_api_key

app = FastAPI()

# Imposta la tua API Key ElevenLabs (da variabile d'ambiente)
API_KEY = os.getenv("ELEVENLABS_API_KEY")
if not API_KEY:
    raise Exception("Variabile ELEVENLABS_API_KEY non impostata!")

set_api_key(API_KEY)

@app.post("/speak")
async def speak(request: Request):
    data = await request.json()
    text = data.get("text")
    voice = data.get("voice", "Bella")  # Voce di default
    
    if not text:
        raise HTTPException(status_code=400, detail="Il testo è obbligatorio")
    
    try:
        # Genera audio in bytes
        audio_bytes = generate(text=text, voice=voice)
        output_path = "output.wav"
        
        # Salva file audio
        save(audio_bytes, output_path)
        
        # Restituisce file audio come risposta
        return FileResponse(output_path, media_type="audio/wav", filename=output_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore nella generazione audio: {str(e)}")

# Endpoint di test base
@app.get("/")
async def root():
    return {"message": "Massimo AI - Text to Speech API attiva"}
