"""
Modulo: multi_language.py
Gestione multilingua di Massimo AI: template, traduzioni, rilevamento lingua utente, personalizzazione contenuti.
Pronto per traduzioni AI o manuali, auto-selezione lingua, onboarding localizzato, template dinamici.
"""

from config import DEFAULT_LANGUAGE, ALLOWED_LANGUAGES

# Dizionario di esempio (va ampliato)
TRANSLATIONS = {
    "it": {
        "welcome": "Ciao {name}, benvenuto in Massimo AI!",
        "level_up": "Hai sbloccato un nuovo livello: {level}!"
    },
    "en": {
        "welcome": "Hi {name}, welcome to Massimo AI!",
        "level_up": "You unlocked a new level: {level}!"
    },
    "fr": {
        "welcome": "Bonjour {name}, bienvenue sur Massimo AI!",
        "level_up": "Nouveau niveau débloqué: {level}!"
    }
}

def get_user_language(user):
    # Demo: restituisce la lingua utente (da DB o preferenze, default italiano)
    return user.get("lang", DEFAULT_LANGUAGE)

def translate(key, user, **kwargs):
    lang = get_user_language(user)
    text = TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANGUAGE]).get(key, "")
    return text.format(**kwargs)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    user = {"name": "Luca", "lang": "fr"}
    print(translate("welcome", user, name="Luca"))
