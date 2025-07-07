from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_office_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "💻 *Microsoft Office – Livello 7*\n\n"

        "Suite Office AI: dashboard integrate, automazioni multi-app, Office + AI Assistant, produzione documenti intelligenti, reporting automatico."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
