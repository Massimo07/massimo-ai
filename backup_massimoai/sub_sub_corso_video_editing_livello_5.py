from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_video_editing_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🎬 *Video Editing – Livello 5*\n\n"

        "Video per campagne ADV: struttura storytelling, CTA video, split test e ottimizzazione per conversione."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

