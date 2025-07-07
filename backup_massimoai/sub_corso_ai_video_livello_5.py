from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_ai_video_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🎥 *AI Video – Livello 5*\n\n"

        "Video AI avanzati: multi-lingua, sincronizzazione audio, creazione contenuti seriali per i tuoi funnel."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
