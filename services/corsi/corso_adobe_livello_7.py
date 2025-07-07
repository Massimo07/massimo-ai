from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_adobe_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🖌️ *Adobe Suite – Livello 7*\n\n"

        "Workflow multi-app, branding totale, automazioni AI, produzione contenuti di squadra, plugin avanzati e dashboard personalizzata."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
