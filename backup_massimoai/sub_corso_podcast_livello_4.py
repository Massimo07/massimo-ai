from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_podcast_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast Pro – Livello 4*\n\n"

        "Ospiti, interviste, podcast video, pubblicazione multi-social."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
