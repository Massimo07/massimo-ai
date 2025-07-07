from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_tiktok_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🎵 *TikTok Mastery – Livello 1*\n\n"

        "Crea il tuo profilo TikTok, carica il primo video, usa effetti e hashtag popolari."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
