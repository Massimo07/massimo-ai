from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_ai_copywriting_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *AI Copywriting – Livello 3*\n\n"

        "Storytelling per funnel e presentazioni, script video AI, personalizzazione linguaggio per target diversi."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

