from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_time_management_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "⏳ *Corso Time Management – Livello 3*\n\n"

        "Gestisci progetti complessi e obiettivi a lungo termine. Strumenti avanzati (Asana, Notion, Gantt) e metodi per delegare."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
