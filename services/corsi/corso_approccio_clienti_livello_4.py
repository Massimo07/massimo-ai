from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_approccio_clienti_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🧑‍💼 *Corso Approccio Clienti – Livello 4*\n\n"

        "Come approcciare nuovi clienti, primi messaggi su social, lista contatti caldi e freddi, domande strategiche e risposte smart."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
