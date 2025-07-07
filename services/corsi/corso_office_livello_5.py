from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_office_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "💻 *Microsoft Office – Livello 5*\n\n"

        "Word: macro base, gestione revisioni. Excel: macro, automazioni, dashboard avanzate. PowerPoint: presentazioni interattive. Outlook: workflow automatizzati."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
