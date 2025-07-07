from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_mentalita_milionario_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Mentalità del Milionario Master – Livello 7*\n\n"

        "Mentalità dei top 1%, segreti degli imprenditori seriali, strategie per impatto globale e legacy familiare."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
