from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_autotraining_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🧘 *Autotraining & Meditazione – Livello 3*\n\n"

        "Visualizzazione positiva: come visualizzare i tuoi obiettivi di network e rafforzare l’autostima ogni giorno."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

