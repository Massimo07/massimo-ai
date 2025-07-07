from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_ai_video_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🎥 *AI Video – Livello 4*\n\n"

        "Automazione produzione video, strumenti AI di editing, storyboard automatico."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

