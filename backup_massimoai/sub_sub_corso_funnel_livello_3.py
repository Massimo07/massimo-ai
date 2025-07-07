from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_funnel_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🛒 *Funnel – Livello 3*\n\n"

        "Gestisci le prime automazioni (mail/SMS), trigger base e come segmentare i contatti."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

