from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_youtube_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "📺 *YouTube Mastery – Livello 2*\n\n"

        "Editing video semplice, miniature personalizzate, playlist, ottimizzazione SEO base per YouTube."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
