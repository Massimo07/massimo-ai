from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_ai_video_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🎥 *AI Video – Livello 6*\n\n"

        "Video marketing automation, video funnel automatizzati, editing in tempo reale AI."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

