from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_video_editing_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🎬 *Video Editing – Livello 6*\n\n"

        "Animazioni avanzate (After Effects), grafiche animate, effetti green screen, editing per webinar e video training."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
