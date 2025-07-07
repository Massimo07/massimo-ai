import json
import os

# Cartella dove hai tutti i file lingua (es: en.json, it.json, ecc.)
I18N_DIR = os.path.join(os.path.dirname(__file__), "../i18n")

# Cache dei dizionari lingua
translations = {}

def load_language(lang_code):
    """Carica il file di traduzione per la lingua richiesta"""
    path = os.path.join(I18N_DIR, f"{lang_code}.json")
    if not os.path.exists(path):
        # Fallback su inglese se la lingua non esiste
        path = os.path.join(I18N_DIR, "en.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def translate(key, lang_code):
    """
    Traduci una chiave per la lingua richiesta.
    Se non trova, restituisce la chiave originale.
    """
    if lang_code not in translations:
        translations[lang_code] = load_language(lang_code)
    return translations[lang_code].get(key, key)
