from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_analytics_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "📊 *Analytics – Livello 6*\n\n"

        "Analisi multilivello, dashboard avanzate per team, export Excel, A/B test funnel, report finanziari e forecast AI."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
