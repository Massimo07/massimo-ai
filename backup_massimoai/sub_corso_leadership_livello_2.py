from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_leadership_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "👑 *Corso Leadership – Livello 2*\n\n"

        "Guida il tuo primo gruppo: come motivare i primi collaboratori, dare feedback costruttivi, organizzare una piccola riunione."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
