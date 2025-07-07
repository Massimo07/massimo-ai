from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_mentalita_milionario_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Mentalità del Milionario – Livello 4*\n\n"

        "Pensiero abbondante, investire in se stessi e negli altri, moltiplicare risorse e creare valore."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
