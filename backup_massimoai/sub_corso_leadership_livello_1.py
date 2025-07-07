from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_leadership_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "👑 *Corso Leadership – Livello 1*\n\n"

        "Sviluppa la leadership personale per essere esempio per il tuo team.\n"

        "Modulo 1: Cos’è la leadership?\n"

        "Modulo 2: Il potere dell’esempio\n"

        "Esercizio pratico: scegli il tuo valore guida."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
