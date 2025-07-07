from langdetect import detect

def detect_language(text):
    """
    Rileva la lingua dal testo usando langdetect (supporta decine di lingue!).
    """
    try:
        return detect(text)
    except Exception:
        return "en"  # fallback su inglese in caso di errore
