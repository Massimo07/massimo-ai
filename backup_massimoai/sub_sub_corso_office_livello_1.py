from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_office_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "💻 *Microsoft Office – Livello 1*\n\n"

        "Introduzione alla suite Office: come scrivere un testo base in Word, creare una tabella in Excel, preparare la prima slide con PowerPoint e inviare una mail semplice da Outlook."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

