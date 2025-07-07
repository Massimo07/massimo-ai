from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_podcast_radio_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast & Radio Master – Livello 7*\n\n"

        "Podcast/Radio internazionale, avatar vocali AI, traduzioni automatiche, streaming su canali globali."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
