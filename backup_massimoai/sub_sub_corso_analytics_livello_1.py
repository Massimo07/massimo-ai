from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_analytics_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "📊 *Analytics – Livello 1*\n\n"

        "Cosa sono i dati? Impara a leggere i numeri principali (ordini, iscrizioni, visualizzazioni base)."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

