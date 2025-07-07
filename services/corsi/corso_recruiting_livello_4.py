from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_recruiting_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🧲 *Corso Recruiting – Livello 4*\n\n"

        "Tecniche base di ricerca, invito a presentazioni online, primi script di invito, come superare i no con il sorriso."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
