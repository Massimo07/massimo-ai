from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_comunicazione_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🗣️ *Corso Comunicazione – Livello 3*\n\n"

        "Public speaking, gestione delle emozioni, come parlare in pubblico dal vivo e online. Allenamento pratico."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
