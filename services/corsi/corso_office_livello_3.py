from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_office_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "💻 *Microsoft Office – Livello 3*\n\n"

        "Word: stili, sommario automatico, modelli. Excel: filtri, funzioni, grafici avanzati. PowerPoint: video e audio nelle presentazioni. Outlook: calendario e gestione regole."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
