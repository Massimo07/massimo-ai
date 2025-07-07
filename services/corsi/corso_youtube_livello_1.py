from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_youtube_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "📺 *YouTube Mastery – Livello 1*\n\n"

        "Apri il tuo canale, carica il primo video, regole base per titoli e descrizioni efficaci."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
