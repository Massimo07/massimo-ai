from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_prodotti_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "📦 *Corso Prodotti – Livello 3*\n\n"

        "Strategie di storytelling per ogni linea, come trasmettere i benefici, creare curiosità, testimonianze clienti reali."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

