from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler, ContextTypes

filters,

filters, ContextTypes

# Lista bandiere europee + cinese + araba

LANGUAGES = [

    ("it", "🇮🇹 Italiano"), ("en", "🇬🇧 English"), ("fr", "🇫🇷 Français"),

    ("de", "🇩🇪 Deutsch"), ("es", "🇪🇸 Español"), ("pt", "🇵🇹 Português"),

    ("ro", "🇷🇴 Română"), ("nl", "🇳🇱 Nederlands"), ("el", "🇬🇷 Ελληνικά"),

    ("ru", "🇷🇺 Русский"), ("ar", "🇸🇦 العربية"), ("zh", "🇨🇳 中文"),

    # Aggiungi altre lingue qui

]

WELCOME_MSG = {

    "it": "Benvenuto in Massimo AI! 🚀\nQui il successo è per tutti. Scegli la tua lingua e inizia il tuo viaggio verso il cambiamento!",

    "en": "Welcome to Massimo AI! 🚀\nHere, success is for everyone. Choose your language and start your journey to change!",

    "fr": "Bienvenue sur Massimo AI ! 🚀\nIci, le succès est pour tous. Choisissez votre langue et commencez votre parcours vers le changement !",

    "de": "Willkommen bei Massimo AI! 🚀\nHier ist Erfolg für alle da. Wähle deine Sprache und beginne deine Reise zur Veränderung!",

    "es": "¡Bienvenido a Massimo AI! 🚀\nAquí el éxito es para todos. ¡Elige tu idioma y empieza tu viaje hacia el cambio!",

    "pt": "Bem-vindo ao Massimo AI! 🚀\nAqui o sucesso é para todos. Escolha seu idioma e comece sua jornada para a mudança!",

    "ro": "Bine ai venit la Massimo AI! 🚀\nAici, succesul este pentru toți. Alege limba ta și începe călătoria spre schimbare!",

    "nl": "Welkom bij Massimo AI! 🚀\nHier is succes voor iedereen. Kies je taal en begin aan je reis naar verandering!",

    "el": "Καλώς ήρθατε στο Massimo AI! 🚀\nΕδώ η επιτυχία είναι για όλους. Επιλέξτε τη γλώσσα σας και ξεκινήστε το ταξίδι σας προς την αλλαγή!",

    "ru": "Добро пожаловать в Massimo AI! 🚀\nЗдесь успех для всех. Выберите свой язык и начните путь к переменам!",

    "ar": "مرحبًا بك في Massimo AI! 🚀\nهنا النجاح للجميع. اختر لغتك وابدأ رحلتك نحو التغيير!",

    "zh": "欢迎来到 Massimo AI！🚀\n这里每个人都能成功。选择你的语言，开启你的改变之旅！"

}

async async async def onboarding_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Mostra immagine di benvenuto (se vuoi aggiungerla) + testo motivazionale

    chat_id = update.effective_chat.id

    keyboard = [

        [InlineKeyboardButton(flag, callback_data=code)] for code, flag in LANGUAGES

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(

        chat_id=chat_id,

        text="🌍 Scegli la tua lingua / Choose your language:",

        reply_markup=reply_markup

    )

async async async def language_chosen(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    code = query.data

    user = get_user(query.from_user.id)

    user['lang'] = code

    await query.answer()

    # Frase motivazionale personalizzata

    welcome_text = WELCOME_MSG.get(code, WELCOME_MSG["it"])

    await query.edit_message_text(

        text=f"{welcome_text}\n\nCome ti chiami? / What's your name?"

    )

    # Dopo che l'utente scrive il nome, passa al menu servizi

# Gestisci inserimento nome utente (scrivi tu la funzione che salva e poi fa partire i bottoni servizi)

onboarding_handlers = [

    ("command", "start", onboarding_start),

    ("callback", LANGUAGES, language_chosen),

    # qui inserisci gli altri passaggi se vuoi

]

