import os
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from dotenv import load_dotenv
import tempfile

load_dotenv()
router = APIRouter()

# ---- TEXT TO SPEECH (TTS) ----

class TTSRequest(BaseModel):
    text: str

@router.post("/voce/tts", tags=["Voce AI"])
async def text_to_speech(req: TTSRequest):
    """
    Genera audio da testo (usa ElevenLabs se API key presente, altrimenti pyttsx3 locale)
    """
    eleven_key = os.getenv("ELEVENLABS_API_KEY")
    if eleven_key:
        try:
            import elevenlabs
            audio = elevenlabs.generate(
                text=req.text,
                api_key=eleven_key,
                voice=os.getenv("ELEVENLABS_VOICE", "Bella")
            )
            filename = "massimo_ai_tts.mp3"
            with open(filename, "wb") as f:
                f.write(audio)
            return {"audio_file": filename}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Errore ElevenLabs: {e}")
    else:
        # Fallback locale (solo su PC, non sempre in cloud)
        try:
            import pyttsx3
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            engine = pyttsx3.init()
            engine.save_to_file(req.text, tmp.name)
            engine.runAndWait()
            tmp.close()
            return {"audio_file": tmp.name}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Errore locale TTS: {e}")


# ---- SPEECH TO TEXT (STT) ----

@router.post("/voce/stt", tags=["Voce AI"])
async def speech_to_text(audio: UploadFile = File(...)):
    """
    Trascrive audio in testo (locale con SpeechRecognition, fallback)
    """
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(await audio.read())
            tmp.close()
            with sr.AudioFile(tmp.name) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data, language="it-IT")
        return {"trascrizione": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore STT: {e}")
