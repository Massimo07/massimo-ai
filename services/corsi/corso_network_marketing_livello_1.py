from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_network_marketing_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🌐 *Corso Network Marketing – Livello 1*\n\n"

        "Introduzione al network marketing: cos’è, come funziona, le regole d’oro per iniziare e le differenze tra venditore, consumatore, networker."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
