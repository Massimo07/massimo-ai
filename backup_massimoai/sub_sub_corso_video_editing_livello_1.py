from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_video_editing_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🎬 *Video Editing – Livello 1*\n\n"

        "Introduzione ai video per social: app semplici (CapCut, InShot), tagliare clip, aggiungere musica e testo base."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

