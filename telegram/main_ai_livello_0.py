# MASSIMO AI - MAIN UNICO LIVELLO 0 (versione FIXATA e ordinata)
import logging
import os
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, MessageHandler, CallbackQueryHandler,
    filters, ContextTypes
)
from dotenv import load_dotenv

# 1. --- CONFIGURAZIONE BASE ---
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
DATA_DIR = "data/"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 2. --- UTILITY GESTIONE UTENTI ---
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
        USERS[uid] = {"lang": "", "name": "", "level": 0, "state": "choosing_language"}
    return USERS[uid]

# 3. --- LINGUE E BANDIERE ---
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
    "zh": "🇨🇳 中文"
}
def get_language_keyboard():
    keyboard = [
        [InlineKeyboardButton(v, callback_data=f"lang_{k}")]
        for k, v in LANGS.items()
    ]
    return InlineKeyboardMarkup(keyboard)

# 4. --- MENU LIVELLO 0 ---
def get_main_menu_keyboard(lang="it"):
    buttons = [
        ("📈 Cos’è il Network Marketing", "network_marketing"),
        ("🏢 Chi è Live On Plus", "presentazione_azienda"),
        ("💎 Il nostro Piano Marketing", "piano_marketing"),
        ("🔄 Differenze: venditore, consumatore, networker", "differenze"),
        ("💰 Perché scegliere Live On Plus", "perche_liveonplus"),
        ("👑 Perché scegliere il Magic Team", "perche_magicteam"),
        ("❓ FAQ", "faq"),
        ("🌟 Motivazione del Giorno", "motivazione_giorno"),
        ("🛍️ Prodotti & Cataloghi", "prodotti_cataloghi"),
        ("📝 Registrati", "registrati"),
        ("🤔 Sei indeciso? Dimmi perché…", "indeciso"),
        ("🫂 Momento no? Parliamone…", "parliamone"),
        ("📚 Scarica il libro", "libro"),
        ("🎤 Eventi e Webinar", "eventi_webinar"),
        ("📰 Aggiornamenti & News", "news"),
        ("🔄 Vuoi vendere o fare autoconsumo?", "venditore_autoconsumo"),
        ("💳 Abbonati e scopri cosa posso offrirti", "abbonati"),
        ("🗣️ Testimonianze vere", "testimonianze"),
        ("💬 Scrivi al tuo sponsor/team", "scrivi_sponsor"),
        ("🤝 Aiuta un amico", "aiuta_amico"),
        ("💡 Feedback su Massimo AI", "feedback_ai"),
        ("🎬 Mini-video guida", "video_guida"),
        # ...fino a 40 bottoni totali, puoi estendere
    ]
    keyboard = [
        [InlineKeyboardButton(txt, callback_data=cb)] for txt, cb in buttons
    ]
    keyboard.append([InlineKeyboardButton("⬅️ Torna indietro", callback_data='back')])
    keyboard.append([InlineKeyboardButton("🏠 Torna alla Home", callback_data='home')])
    return InlineKeyboardMarkup(keyboard)

# 5. --- ONBOARDING SENZA /START: SOLO BANDIERE ---
async def handle_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    user["state"] = "choosing_language"
    save_users(USERS)
    await update.message.reply_text(
        "🌍 Scegli la tua lingua e partiamo!!!",
        reply_markup=get_language_keyboard(),
        parse_mode="HTML"
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
        "✨ Prima di tutto presentiamoci: io sono Massimo AI, il tuo alleato! E tu? Come ti chiami? Scrivilo qui sotto, non vedo l’ora di accompagnarti nel tuo percorso. 😃"
    )

async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    if user["state"] == "onboarding_name":
        name = update.message.text.strip()
        user["name"] = name
        user["state"] = "main_menu"
        save_users(USERS)
        await update.message.reply_text(
            f"Ciao {name}! 👋 Benvenuto/a su Massimo AI.\nEcco tutto ciò che puoi scoprire:",
            reply_markup=get_main_menu_keyboard(user["lang"])
        )
    else:
        await update.message.reply_text("Rispondi alla domanda precedente per favore.")

# 6. --- ROUTING MENU PRINCIPALE ---
async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    user_id = query.from_user.id
    user = get_user(user_id)
    await query.answer()
    if data == "network_marketing":
        await query.edit_message_text("Il network marketing è una risorsa straordinaria perché...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "presentazione_azienda":
        await query.edit_message_text("Qui puoi scaricare la presentazione PDF di Live On Plus!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "piano_marketing":
        await query.edit_message_text("Qui trovi il nostro piano marketing (PDF): studialo per scoprire tutte le opportunità!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "differenze":
        await query.edit_message_text("Ecco le differenze tra venditore, consumatore e networker...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "perche_liveonplus":
        await query.edit_message_text("Scegli Live On Plus perché offre vantaggi reali: sconti, prodotti esclusivi e supporto!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "perche_magicteam":
        await query.edit_message_text("Il Magic Team è speciale per ambiente, risultati e... la presenza di Massimo! 🏆", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "faq":
        await query.edit_message_text("FAQ - Domande Frequenti:\n- Come acquistare?\n- Come ottenere sconto?\n...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "motivazione_giorno":
        await query.edit_message_text("La motivazione di oggi: \"Credi in te stesso e vola alto!\"", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "prodotti_cataloghi":
        await query.edit_message_text("Prodotti & Cataloghi:\n- Chiedimi che prodotto ti serve!\n- Scarica i cataloghi PDF...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "registrati":
        await query.edit_message_text("Compila il form di registrazione e scegli il tuo sponsor...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "indeciso":
        await query.edit_message_text("Raccontami perché sei indeciso: Massimo AI ti ascolta e risponde.", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "parliamone":
        await query.edit_message_text("Hai un momento no? Scrivimi: sono qui per ascoltarti e darti una mano! 🤗", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "libro":
        await query.edit_message_text("Scarica il libro di Massimo qui: [link]", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "eventi_webinar":
        await query.edit_message_text("Eventi e Webinar Live On Plus/Magic Team: elenco aggiornato...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "news":
        await query.edit_message_text("Lascia la tua email/whatsapp per ricevere tutte le news!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "venditore_autoconsumo":
        await query.edit_message_text("Vuoi vendere o essere cliente? Registrati qui, scegli sponsor, ricevi codice LOP...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "abbonati":
        await query.edit_message_text("Ecco tutti i livelli di abbonamento Massimo AI! Scegli quello giusto per te e scopri cosa sblocchi...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "testimonianze":
        await query.edit_message_text("Cosa dicono gli altri? Leggi le testimonianze di chi ha già scelto Magic Team...", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "scrivi_sponsor":
        await query.edit_message_text("Vuoi parlare col tuo sponsor o il team? Scrivici direttamente!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "aiuta_amico":
        await query.edit_message_text("Aiuta un amico a scoprire Massimo AI: condividi questa info!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "feedback_ai":
        await query.edit_message_text("Lascia un feedback su Massimo AI per aiutarci a migliorare!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "video_guida":
        await query.edit_message_text("Mini-video guida: ecco come funziona il bot passo passo.", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "back":
        await query.edit_message_text("Torna alla schermata precedente!", reply_markup=get_main_menu_keyboard(user["lang"]))
    elif data == "home":
        await query.edit_message_text("Menu principale Massimo AI:", reply_markup=get_main_menu_keyboard(user["lang"]))
    else:
        await query.edit_message_text("Servizio in arrivo!", reply_markup=get_main_menu_keyboard(user["lang"]))

# 7. --- AVVIO BOT ---
def main():
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), handle_entry))
    app.add_handler(CallbackQueryHandler(handle_language, pattern="^lang_"))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_name))
    app.add_handler(CallbackQueryHandler(handle_menu))
    print("Massimo AI Livello 0 definitivo in esecuzione...")
    app.run_polling()
    save_users(USERS)

if __name__ == "__main__":
    main()
