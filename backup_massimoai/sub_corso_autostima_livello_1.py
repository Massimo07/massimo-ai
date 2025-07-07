from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_autostima_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "💪 *Corso Autostima – Livello 1*\n\n"

        "Scopri cosa significa autostima, il valore di credere in te stesso e inizia un esercizio base di gratitudine giornaliera."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
