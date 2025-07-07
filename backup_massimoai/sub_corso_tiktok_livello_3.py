from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_tiktok_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🎵 *TikTok Mastery – Livello 3*\n\n"

        "Viralità, challenge, TikTok LIVE, commenti e analisi prime statistiche."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
