from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_podcast_radio_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast & Radio – Livello 1*\n\n"

        "Cos’è un podcast? Differenza tra podcast e radio. Come ascoltare contenuti audio e trovare ispirazione."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
