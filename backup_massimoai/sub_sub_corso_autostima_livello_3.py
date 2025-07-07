from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_autostima_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "💪 *Corso Autostima – Livello 3*\n\n"

        "Potenzia la tua resilienza: tecniche per affrontare fallimenti, sviluppare una mentalità vincente, auto-motivarsi ogni giorno."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

