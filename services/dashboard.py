from telegram import Update
from telegram.ext import ContextTypes

async def dashboard_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menu principale admin."""
    keyboard = [
        [("Export utenti", "export_utenti")],
        [("Statistiche", "stats")],
        [("Log sistema", "logs")],
        [("Banna utente", "ban_user")],
    ]
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    markup = InlineKeyboardMarkup([[InlineKeyboardButton(txt, callback_data=cb)] for txt, cb in keyboard])
    await update.message.reply_text("Benvenuto nell'area admin di Massimo AI.\nScegli una funzione:", reply_markup=markup)
