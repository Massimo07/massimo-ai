from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_webinar_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🎤 *Webinar – Livello 6*\n\n"

        "Strategie avanzate: funnel webinar, presentatori multipli, replay automatici, vendita di corsi/servizi in diretta."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

