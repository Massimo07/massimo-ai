from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_automation_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🤖 *Automation Lab – Livello 5*\n\n"

        "Gestione automazioni team, notifiche su Telegram/WhatsApp, workflow collaborativi."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
