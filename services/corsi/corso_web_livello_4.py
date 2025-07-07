from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_web_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🌍 *Corso Web – Livello 4*\n\n"

        "Come creare una pagina personale su siti/landing semplici, collegare il link di iscrizione, tracciare i primi accessi, configurare il profilo Telegram/WhatsApp web."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
