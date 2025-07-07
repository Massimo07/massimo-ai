from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_plugin_automazioni_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🔌 *Plugin & Automazioni – Livello 6*\n\n"

        "Automazioni avanzate, orchestrazione task multipli, monitoraggio AI degli errori, alert predittivi."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
