# ===== main_backend.py =====
import uuid
from datetime import datetime
import random
from fastapi import FastAPI, Request, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

# Se hai file "models.py" e services, importa così:
from models import User, System
from services.stripe_service import create_checkout_session
from services.factory import create_macrosystem
from services.agent_manager import dispatch_agent
from services.voice_service import tts, stt, ask_gpt
from services.translation import translate
from services.sentiment import analyze_sentiment
from services.lang_detect import detect_language

app = FastAPI(title="Massimo AI Neuro-System Definitivo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

users = {}
systems = {}
otp_codes = {}  # cell: otp temporaneo

# ====================
# ROOT
# ====================
@app.get("/")
def root():
    return {"msg": "Welcome to Massimo AI Neuro-System – Definitivo"}

# ====================
# ONBOARDING – MULTILINGUA
# ====================
@app.post("/onboarding/")
async def onboarding(data: dict):
    name = data.get("name")
    cell = data.get("cell")
    email = data.get("email")
    country = data.get("country")
    user_lang = data.get("language", "")
    if not name or not cell or not email or not country:
        raise HTTPException(status_code=400, detail="Tutti i campi obbligatori")
    if not user_lang or user_lang.strip() == "":
        user_lang = detect_language(name)
    user = User(
        id=str(uuid.uuid4()),
        name=name,
        cell=cell,
        email=email,
        country=country,
        language=user_lang,
        signup_date=datetime.now()
    )
    users[user.id] = user
    msg = translate(f"Welcome, {user.name}!", user_lang)
    return {"msg": msg, "user_id": user.id, "language": user_lang}

# ====================
# OTP – INVIO
# ====================
@app.post("/send_otp/")
async def send_otp(data: dict):
    cell = data.get("cell")
    if not cell:
        raise HTTPException(status_code=400, detail="Cell obbligatorio")
    otp = str(random.randint(100000, 999999))
    otp_codes[cell] = otp
    print(f"[DEBUG OTP] Codice {otp} inviato a {cell}")  # In produzione: invia via SMS!
    return {"msg": "OTP inviato"}

# ====================
# OTP – LOGIN
# ====================
@app.post("/login_otp/")
async def login_otp(data: dict):
    cell = data.get("cell")
    otp = data.get("otp")
    if not cell or not otp:
        raise HTTPException(status_code=400, detail="Cell e OTP obbligatori")
    if otp_codes.get(cell) != otp:
        raise HTTPException(status_code=401, detail="OTP non valido")
    # Cerca utente per cell
    for user in users.values():
        if user.cell == cell:
            del otp_codes[cell]
            return {
                "msg": f"Benvenuto di nuovo, {user.name}!",
                "user_id": user.id,
                "profile": {
                    "name": user.name,
                    "cell": user.cell,
                    "email": user.email,
                    "country": user.country,
                    "language": user.language
                }
            }
    raise HTTPException(status_code=404, detail="Utente non trovato")

# ====================
# PILLOLE PREMIUM (per settimana di prova)
# ====================
PILLOLE = [
    "Scopri la dashboard founder: controlla tutto il tuo business in tempo reale.",
    "Vuoi la tua AI personale? Solo abbonandoti puoi crearne una su misura.",
    "Report avanzati sulle tue performance: dati e previsioni per crescere.",
    "Formazione esclusiva AI, con corsi personalizzati solo per gli abbonati.",
    "Supporto emotivo AI: chat 24/7 con il coach motivazionale Massimo AI.",
    "Automazioni business: email, WhatsApp, social… tutto in automatico!",
    "Accesso prioritario alle nuove funzioni e al marketplace degli agenti AI."
]
@app.post("/get_pillola/")
async def get_pillola(data: dict):
    user_id = data.get("user_id")
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    days = (datetime.now() - getattr(user, "signup_date", datetime.now())).days
    idx = min(days, len(PILLOLE)-1)
    return {"pillola": PILLOLE[idx], "day": days+1}

# ====================
# CALCOLO PREZZO ABBONAMENTO
# ====================
@app.get("/pricing/{category}")
def pricing(category: str):
    stipendi = {
        "student": 600, "teacher": 1800, "lawyer": 3000, "manager": 4200,
        "doctor": 3600, "freelancer": 2000, "retired": 1200, "housewife": 900,
        "artist": 1200, "entrepreneur": 3500, "other": 1500
    }
    stipendio = stipendi.get(category.lower(), 1500)
    price = round(stipendio / 6)
    return {"category": category, "monthly_price": price}

# ====================
# CHECKOUT STRIPE
# ====================
@app.post("/stripe/checkout/")
async def stripe_checkout(data: dict):
    user_id = data.get("user_id")
    amount = data.get("amount")
    if not user_id or not amount:
        raise HTTPException(status_code=400, detail="user_id and amount required")
    url = create_checkout_session(user_id, amount)
    return {"checkout_url": url}

# ====================
# MACRO-FACTORY: CREA SISTEMI AI PERSONALIZZATI
# ====================
@app.post("/factory/create/")
async def create_factory(data: dict):
    system = create_macrosystem(data)
    systems[system.id] = system
    return {"msg": "Macrosistema creato", "system_id": system.id}

# ====================
# AI EMPATICA (testo → TTS se serve)
# ====================
@app.post("/ai/respond/")
async def ai_respond(data: dict):
    text = data.get("text")
    lang = data.get("lang", "it")
    if not text:
        raise HTTPException(status_code=400, detail="text required")
    mood = analyze_sentiment(text, lang)
    response = dispatch_agent({"task": text, "mood": mood})
    if data.get("tts", False):
        audio_stream = tts(response, lang)
        if audio_stream:
            return StreamingResponse(audio_stream, media_type="audio/wav", headers={"X-AI-Reply": response})
        else:
            return {"response": response, "audio_error": "TTS failed"}
    return {"response": response, "mood": mood}

# ====================
# DASHBOARD FOUNDER MINIMALE (statistiche demo)
# ====================
@app.get("/dashboard/")
def founder_dashboard():
    return {
        "users": len(users),
        "systems": len(systems),
        "active_subs": sum([1 for u in users.values() if getattr(u, "plan", None)]),
    }

# ====================
# TTS ENDPOINT SEMPLICE (text2audio WAV)
# ====================
@app.post("/speak/")
async def speak(request: Request):
    data = await request.json()
    text = data.get("text")
    lang = data.get("lang", "it")
    voice = data.get("voice", "Bella")
    if not text:
        raise HTTPException(status_code=400, detail="Il testo è obbligatorio")
    audio_stream = tts(text, lang, voice)
    if not audio_stream:
        raise HTTPException(status_code=500, detail="Errore generazione audio")
    return StreamingResponse(audio_stream, media_type="audio/wav")

# ====================
# VOICECHAT: AUDIO IN → TESTO → AI → AUDIO OUT!
# ====================
@app.post("/ai/voicechat/")
async def voice_chat(
    audio: UploadFile = File(None),
    text: str = Form(None),
    lang: str = Form("it"),
    voice: str = Form("Bella")
):
    user_text = ""
    if audio:
        audio_bytes = await audio.read()
        user_text = stt(audio_bytes, lang)
    elif text:
        user_text = text
    else:
        raise HTTPException(status_code=400, detail="Devi fornire audio o testo")
    ai_reply = ask_gpt(user_text, lang)
    audio_stream = tts(ai_reply, lang, voice)
    if audio_stream:
        return StreamingResponse(audio_stream, media_type="audio/wav", headers={"X-AI-Reply": ai_reply})
    else:
        return {"response": ai_reply, "audio_error": "Impossibile generare audio"}

# ====================
# PROPOSTA PERSONALIZZATA FINE SETTIMANA DI PROVA!
# ====================
@app.post("/end_trial/")
async def end_trial(data: dict):
    user_id = data.get("user_id")
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Dati raccolti: da espandere con quello che vuoi loggare!
    settore = getattr(user, "sector", "generico")
    ruolo = getattr(user, "role", "utente")
    guadagno = getattr(user, "income", 1000)
    funzioni_usate = getattr(user, "used_features", [])
    soddisfazione = getattr(user, "satisfaction", 7)

    # Prezzo personalizzato (esempio 1/6 del guadagno)
    prezzo_premium = int(guadagno) // 6
    if prezzo_premium < 20:
        prezzo_premium = 20

    # Crea macrosistema personalizzato
    system_data = {
        "user_id": user_id,
        "sector": settore,
        "role": ruolo,
        "income": guadagno,
        "features": funzioni_usate
    }
    system = create_macrosystem(system_data)
    systems[system.id] = system

    # Risposta con confronto base/personalizzato
    return {
        "msg": "Ecco la tua proposta personalizzata!",
        "confronto": {
            "base": {
                "name": "Massimo AI Base",
                "price": "20€/mese",
                "features": ["Funzioni standard", "Motivazione base", "Prodotti generici", "Nessuna personalizzazione"]
            },
            "personalizzato": {
                "name": system.name,
                "price": f"{prezzo_premium}€/mese",
                "features": system.features,
                "branding": system.branding,
                "dashboard_url": system.dashboard_url
            }
        },
        "scelta": ["Attiva Base", "Attiva Personalizzato", "Parla con Founder"]
    }


# ===== main_api.py =====
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


# ===== test.py =====
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


# ===== test2.py =====
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


# ===== test3.py =====
import os
import logging
from dotenv import load_dotenv
import openai
from elevenlabs import set_api_key, generate

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
VOICE_ID = "ZthjuvLPty3kTMaNKVKb"  # Jackson

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

def main():
    print("==== MASSIMO AI ADVANCED ====")
    testo_utente = input("→ Inserisci la tua domanda per Massimo AI:\n").strip()
    if not testo_utente:
        logger.warning("Input vuoto. Terminato.")
        return
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


# ===== test4.py =====
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


# ===== test5.py =====
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


# ===== pest.py =====
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
