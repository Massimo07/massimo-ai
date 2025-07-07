from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_video_editing_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🎬 *Video Editing – Livello 3*\n\n"

        "Montaggio avanzato: sovrapposizioni, voiceover, sottotitoli, effetti sonori, branding video personalizzato."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
