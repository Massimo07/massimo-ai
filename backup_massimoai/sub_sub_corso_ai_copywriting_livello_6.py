from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_ai_copywriting_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *AI Copywriting – Livello 6*\n\n"

        "A/B test automatici, copywriting neuro-marketing, funnel automation con AI writing."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

