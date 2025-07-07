from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_tiktok_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🎵 *TikTok Mastery – Livello 7*\n\n"

        "Crescita mondiale, strategie da top influencer, monetizzazione internazionale, contenuti AI-first!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
