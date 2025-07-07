from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_analytics_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "📊 *Analytics – Livello 5*\n\n"

        "Automazione report, analisi predittiva, suggerimenti su obiettivi personali, alert su utenti a rischio abbandono."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

