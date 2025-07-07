from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_plugin_automazioni_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🔌 *Plugin & Automazioni – Livello 2*\n\n"

        "Creare reminder automatici, notifiche per appuntamenti, prime integrazioni con tool Live On Plus."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
