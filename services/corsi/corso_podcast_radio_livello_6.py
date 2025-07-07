from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_podcast_radio_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast & Radio – Livello 6*\n\n"

        "Automazioni, estratti automatici, programmazione AI per contenuti vocali e gestione ospiti in remoto."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
