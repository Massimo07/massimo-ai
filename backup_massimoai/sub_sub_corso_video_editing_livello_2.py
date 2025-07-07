from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_video_editing_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🎬 *Video Editing – Livello 2*\n\n"

        "Transizioni, effetti base, prime animazioni e gestione del formato verticale/orizzontale per TikTok e Instagram."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

