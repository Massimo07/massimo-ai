from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_webinar_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🎤 *Webinar – Livello 5*\n\n"

        "Webinar professionali: strumenti Zoom/Meet, co-host, registrazione, condivisione schermo, domande live e sondaggi."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
