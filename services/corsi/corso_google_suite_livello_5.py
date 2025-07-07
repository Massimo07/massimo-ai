from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_google_suite_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🌐 *Google Suite – Livello 5*\n\n"

        "Automazioni Google: Google Apps Script base, notifiche automatiche, moduli avanzati e dashboard personalizzate."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
