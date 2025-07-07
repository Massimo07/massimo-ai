# MASSIMO AI - BOT LIVELLO 0 FREE - PRONTO ALL'USO
import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler,
    filters, ContextTypes, ConversationHandler
)
from dotenv import load_dotenv
import json

# Carica .env (token, ecc.)
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID", "5783601920")
DATA_DIR = "data/"
USERS_FILE = os.path.join(DATA_DIR, "users.json")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ----------- UTILITY ------------

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

USERS = load_users()

def get_user(user_id):
    uid = str(user_id)
    if uid not in USERS:
        USERS[uid] = {"lang": "", "name": "", "level": 0, "first": True, "sponsor": "", "state": "new"}
    return USERS[uid]

# ----------- LINGUE E BANDIERE -----------
LANGS = {
    "it": "🇮🇹 Italiano",
    "en": "🇬🇧 English",
    "es": "🇪🇸 Español",
    "fr": "🇫🇷 Français",
    "de": "🇩🇪 Deutsch",
    "ro": "🇷🇴 Română",
    "pt": "🇵🇹 Português",
    "pl": "🇵🇱 Polski",
    "nl": "🇳🇱 Nederlands",
    "ru": "🇷🇺 Русский",
    "el": "🇬🇷 Ελληνικά",
    "ar": "🇸🇦 العربية",
    "zh": "🇨🇳 中文",
    # altre lingue qui...
}
LANGS_TEXT = " | ".join([f"{v}" for v in LANGS.values()])

def get_language_keyboard():
    keyboard = [
        [InlineKeyboardButton(v, callback_data=f"lang_{k}")]
        for k, v in LANGS.items()
    ]
    return InlineKeyboardMarkup(keyboard)

# ----------- ONBOARDING -----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    user["state"] = "choosing_language"
    save_users(USERS)
    text = "🌍 <b>Scegli la tua lingua e partiamo!!!</b>"
    await update.message.reply_text(
        text, reply_markup=get_language_keyboard(), parse_mode="HTML"
    )

async def handle_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    lang_code = query.data.replace("lang_", "")
    user_id = query.from_user.id
    user = get_user(user_id)
    user["lang"] = lang_code
    user["state"] = "onboarding_name"
    save_users(USERS)
    await query.answer()
    await query.edit_message_text(
        "Perfetto! Ora, come ti chiami?"
    )

async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    if user["state"] == "onboarding_name":
        name = update.message.text.strip()
        user["name"] = name
        user["state"] = "main_menu"
        save_users(USERS)
        text = f"Ciao {name}! 👋\nBenvenuto su Massimo AI. Ecco cosa puoi fare nel Livello 0:\n"
        # Qui mostrerai il menu principale livello 0
        await update.message.reply_text(
            text, reply_markup=get_main_menu_keyboard(user["lang"])
        )
    else:
        await update.message.reply_text("Rispondi alla domanda precedente per favore.")

# ----------- MENU PRINCIPALE LIVELLO 0 (ESEMPLIFICATIVO: QUI INSERISCI I 40 SERVIZI) -----------

def get_main_menu_keyboard(lang):
    # SEMPLICE ESEMPIO con 8 tasti, estendi a 40 con i tuoi servizi reali!
    keyboard = [
        [InlineKeyboardButton("🔍 Prodotti", callback_data="prodotti")],
        [InlineKeyboardButton("🛒 Cataloghi", callback_data="cataloghi")],
        [InlineKeyboardButton("💡 Motivazione", callback_data="motivazione")],
        [InlineKeyboardButton("🧑‍🤝‍🧑 Magic Team", callback_data="magicteam")],
        [InlineKeyboardButton("🤝 Scegli Sponsor", callback_data="sponsor")],
        [InlineKeyboardButton("❓ FAQ", callback_data="faq")],
        [InlineKeyboardButton("💬 Se vuoi ti posso aiutare", callback_data="supporto")],
        [InlineKeyboardButton("🏠 Home", callback_data="home")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ----------- HANDLERS PER I TASTI MENU PRINCIPALE --------------

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    user_id = query.from_user.id
    user = get_user(user_id)
    await query.answer()
    if data == "prodotti":
        await query.edit_message_text("Qui trovi tutti i prodotti Live On Plus (elenco dinamico...)", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "cataloghi":
        await query.edit_message_text("Qui trovi i cataloghi PDF da sfogliare...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "motivazione":
        await query.edit_message_text("Ecco la frase motivazionale del giorno: 'Non smettere mai di crederci!' 💎", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "magicteam":
        await query.edit_message_text("Perché scegliere il Magic Team? Supporto, crescita, risultati!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "sponsor":
        await query.edit_message_text("Scegli il tuo sponsor preferito dalla lista!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "faq":
        await query.edit_message_text("Domande Frequenti:\n- Come acquistare?\n- Come ottenere lo sconto?\n- ...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "supporto":
        await query.edit_message_text("Scrivimi se vuoi parlare o hai bisogno di aiuto, sono qui per ascoltarti! 💬", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "home":
        await query.edit_message_text("Sei tornato alla Home.", reply_markup=get_main_menu_keyboard(user["lang"]))
    else:
        await query.edit_message_text("Servizio in arrivo!", reply_markup=get_main_menu_keyboard(user["lang"]))

# ----------- AVVIO DEL BOT --------------

def main():
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_language, pattern="^lang_"))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_name))
    app.add_handler(CallbackQueryHandler(handle_menu))
    print("Massimo AI Livello 0 in esecuzione...")
    app.run_polling()
    save_users(USERS)

if __name__ == "__main__":
    main()
