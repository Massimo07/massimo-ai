from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_time_management_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "⏳ *Corso Time Management – Livello 1*\n\n"

        "Gestisci meglio il tempo fin da subito.\n"

        "Modulo 1: Cosa significa gestire il tempo\n"

        "Modulo 2: Eliminare le distrazioni\n"

        "Esercizio pratico: la to-do list semplice."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
