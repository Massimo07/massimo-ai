from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_vendita_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "💼 *Corso Vendita – Livello 3*\n\n"

        "Tecniche di chiusura: urgenza, scarsità, gestione delle ultime obiezioni e follow-up automatico con strumenti digitali."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
