from telegram import Update
from telegram.ext import ContextTypes

async def logs_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostra ultimi log di sistema (esempio dummy)."""
    # Qui puoi leggere i log reali dal file o da variabile
    logs = ["2025-06-26 13:00 - Login admin", "2025-06-26 13:01 - Export utenti"]
    await update.callback_query.message.reply_text("\n".join(logs[-10:]))
