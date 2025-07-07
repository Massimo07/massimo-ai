from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
LANGUAGES = {

    "it": "🇮🇹",

    "en": "🇬🇧",

    "es": "🇪🇸",

    "fr": "🇫🇷",

    "de": "🇩🇪",

    "ro": "🇷🇴",

    "ru": "🇷🇺",

    "nl": "🇳🇱",

    "pl": "🇵🇱",

    "ar": "🇸🇦",

    "zh": "🇨🇳",

    # ...altre

}

TRANSLATIONS = {

    "it": {

        "choose_language": "Scegli la tua lingua",

        "welcome": "Benvenuto su Massimo AI!",

        "ask_name": "Come ti chiami?",

        "thanks_name": "Grazie e benvenuto,",

        "choose_avatar": "Preferisci essere seguito da un avatar uomo o donna?",

        "onboarding_complete": "Onboarding completato! Ora puoi esplorare tutte le funzioni.",

        "amico": "Amico",

        "main_menu": "Menu principale,",

        "current_level": "Livello attuale:",

        "cos_e_nm": "Cos'è il Network Marketing?",

        "chi_e_lop": "Chi è Live On Plus",

        "piano_marketing": "Il nostro piano marketing",

        "differenze": "Differenze: venditore, consumatore, networker",

        "perche_lop": "Perché scegliere Live On Plus",

        "perche_magic_team": "Perché scegliere il Magic Team",

        "faq": "FAQ",

        "motivazione_giorno": "Motivazione del Giorno",

        "prodotti_cataloghi": "Prodotti & Cataloghi",

        "registrati": "Registrati",

        "sei_indeciso": "Sei indeciso? Dimmi perché…",

        "momento_no": "Momento no? Parliamone…",

        "scarica_libro": "Scarica il libro",

        "eventi_webinar": "Eventi & Webinar",

        "aggiornamenti_news": "Aggiornamenti & News",

        "vendita_autoconsumo": "Vuoi vendere o fare autoconsumo?",

        "abbonati_scopri": "Abbonati e scopri cosa posso offrirti",

        "motivazione_ai": "✨ Motivazione AI:"

    },

    "en": {

        "choose_language": "Choose your language",

        "welcome": "Welcome to Massimo AI!",

        "ask_name": "What's your name?",

        "thanks_name": "Thank you and welcome,",

        "choose_avatar": "Would you like to be followed by a male or female avatar?",

        "onboarding_complete": "Onboarding complete! Now you can explore all features.",

        "amico": "Friend",

        "main_menu": "Main menu,",

        "current_level": "Current level:",

        # ...traduzioni degli altri tasti come sopra

        "motivazione_ai": "✨ AI Motivation:"

    },

    # ...altre lingue

}

def t(key, lang="it"):

    return TRANSLATIONS.get(lang, TRANSLATIONS["it"]).get(key, key)

