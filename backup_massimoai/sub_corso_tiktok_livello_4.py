from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_tiktok_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🎵 *TikTok Mastery – Livello 4*\n\n"

        "Strategie contenuti seriali, automatizza programmazione video, playlist TikTok."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
