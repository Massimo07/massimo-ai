from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_vendita_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "💼 *Corso Vendita – Livello 2*\n\n"

        "Gestione delle obiezioni: tecniche per rispondere con empatia e sicurezza, casi pratici reali."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
