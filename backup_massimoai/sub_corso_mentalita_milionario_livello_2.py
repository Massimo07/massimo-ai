from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_mentalita_milionario_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Mentalità del Milionario – Livello 2*\n\n"

        "Abitudini vincenti: routine quotidiana, gestione del tempo come i ricchi, disciplina e costanza nei piccoli gesti."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
