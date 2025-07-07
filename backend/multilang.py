import json
import os

# Sostituisci con la tua funzione AI di traduzione, qui demo
from services.translation import ai_translate

def get_text(key, lang="it"):
    """
    Recupera la frase localizzata.
    Se non esiste in JSON, traduce la chiave con l'intelligenza artificiale.
    """
    try:
        path = os.path.join(os.path.dirname(__file__), "../i18n", f"{lang}.json")
        with open(path, encoding="utf-8") as f:
            texts = json.load(f)
        if key in texts:
            return texts[key]
        # fallback: AI translate della chiave/etichetta
        return ai_translate(key, target_lang=lang)
    except Exception:
        # fallback estremo: traduci con AI anche se manca il file
        return ai_translate(key, target_lang=lang)
