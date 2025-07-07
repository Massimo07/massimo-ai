from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_analytics_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "📊 *Analytics – Livello 5*\n\n"

        "Automazione report, analisi predittiva, suggerimenti su obiettivi personali, alert su utenti a rischio abbandono."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
