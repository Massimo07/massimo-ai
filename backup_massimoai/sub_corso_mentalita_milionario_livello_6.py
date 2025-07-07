from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_mentalita_milionario_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Mentalità del Milionario – Livello 6*\n\n"

        "Gestione avanzata delle entrate, moltiplicare i flussi di reddito, controllo delle spese e investimento intelligente."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
