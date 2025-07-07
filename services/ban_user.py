from telegram import Update
from telegram.ext import ContextTypes
from utils import USERS, save_all_users

async def ban_user_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Banna un utente (deve ricevere user_id come argomento nel comando)."""
    query = update.callback_query
    if context.args:
        user_id = context.args[0]
        if user_id in USERS:
            USERS[user_id]["banned"] = True
            save_all_users()
            await query.message.reply_text(f"✅ Utente {user_id} bannato.")
        else:
            await query.message.reply_text("User ID non trovato.")
    else:
        await query.message.reply_text("Devi specificare l'user_id da bannare.")
