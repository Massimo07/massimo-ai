from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_vendita_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "💼 *Corso Vendita – Livello 1*\n\n"

        "Le basi della vendita: ascolto, empatia, domande.\n"

        "Modulo 1: Capire il cliente\n"

        "Modulo 2: Presentare il prodotto\n"

        "Quiz: simulazione conversazione."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
