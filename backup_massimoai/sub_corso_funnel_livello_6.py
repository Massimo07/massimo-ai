from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_funnel_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🛒 *Funnel – Livello 6*\n\n"

        "Personalizzazione massima: funnel multi-lingua, offerte dinamiche, retargeting avanzato."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
