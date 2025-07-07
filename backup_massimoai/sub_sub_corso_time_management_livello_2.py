from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_time_management_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "⏳ *Corso Time Management – Livello 2*\n\n"

        "Tecniche di pianificazione avanzata, come creare routine efficaci, strumenti digitali (Google Calendar, Trello)."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

