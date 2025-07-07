from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_mentalita_milionario_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Mentalità del Milionario – Livello 5*\n\n"

        "Networking di successo: circondarsi di vincenti, creare partnership, imparare dagli errori dei grandi."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

