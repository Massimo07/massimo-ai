from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_video_editing_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🎬 *Video Editing – Livello 4*\n\n"

        "Editing con Adobe Premiere/DaVinci: tagli professionali, color grading base, esportazione in alta qualità."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

