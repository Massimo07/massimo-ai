from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_network_marketing_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🌐 *Corso Network Marketing – Livello 1*\n\n"

        "Introduzione al network marketing: cos’è, come funziona, le regole d’oro per iniziare e le differenze tra venditore, consumatore, networker."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

