from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_mentalita_milionario_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Mentalità del Milionario – Livello 3*\n\n"

        "Visione a lungo termine, fissare obiettivi ambiziosi, gestione delle emozioni nelle decisioni economiche."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
