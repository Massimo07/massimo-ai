from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_automation_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🤖 *Automation Lab – Livello 1*\n\n"

        "Cos’è l’automazione? Primi passi con Zapier/Make, automatizza una notifica email."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
