from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json

import os

USERS_PATH = "data/users.json"

USERS = {}

# Carica tutti gli utenti dal file JSON

def load_all_users():

    global USERS

    if os.path.exists(USERS_PATH):

        with open(USERS_PATH, "r", encoding="utf-8") as f:

            USERS = json.load(f)

    else:

        USERS = {}

# Salva tutti gli utenti su file JSON

def save_all_users():

    with open(USERS_PATH, "w", encoding="utf-8") as f:

        json.dump(USERS, f, ensure_ascii=False, indent=2)

# Restituisce (e crea se serve) il profilo di un utente

def get_user(user_id):

    user_id_str = str(user_id)

    if user_id_str not in USERS:

        USERS[user_id_str] = {

            "name": "",

            "lang": "it",

            "level": 0,

            "registered": False,

            "sponsor": "",

            "code": "",

            "quiz_done": False,

            "support": "",

            "faq_done": False,

            "city": "",

            "province": "",

            "email": "",

            "phone": "",

        }

    return USERS[user_id_str]

# Utility: aggiorna un campo utente e salva subito

def set_user(user_id, key, value):

    u = get_user(user_id)

    u[key] = value

    save_all_users()

# Pulsanti di navigazione (da usare in tutte le tastiere inline)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_navigation_keyboard(extra_buttons=None, lang="it"):

    keyboard = []

    if extra_buttons:

        keyboard.extend(extra_buttons)

    keyboard.append([InlineKeyboardButton("⬅️ Torna indietro", callback_data='back')])

    keyboard.append([InlineKeyboardButton("🏠 Torna alla Home", callback_data='home')])

    return InlineKeyboardMarkup(keyboard)

# Fallback universale

async async def fallback_handler(update, context):

    if update.message:

        await update.message.reply_text("Non ho capito, riprova dal menu!")

    elif update.callback_query:

        update.callback_query.answer("Non ho capito, riprova dal menu!")

# Utility per traduzioni rapide (placeholder, migliora a piacere)

LANGS = {

    "it": "🇮🇹 Italiano",

    "en": "🇬🇧 English",

    "es": "🇪🇸 Español",

    "fr": "🇫🇷 Français",

    "de": "🇩🇪 Deutsch",

    "ro": "🇷🇴 Română",

    "pt": "🇵🇹 Português",

    "nl": "🇳🇱 Nederlands",

    "el": "🇬🇷 Ελληνικά",

    "ru": "🇷🇺 Русский",

    "ar": "🇸🇦 العربية",

    "zh": "🇨🇳 中文",

}

def get_lang_flag(lang):

    return LANGS.get(lang, "🌐")

# All’avvio del bot carica subito gli utenti

load_all_users()

