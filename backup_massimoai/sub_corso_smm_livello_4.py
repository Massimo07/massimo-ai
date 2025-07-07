from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_smm_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "📣 *Corso Social Media Manager – Livello 4*\n\n"

        "Gestione contenuti multi-canale: piano editoriale, programmazione post, rispondere ai commenti e prime automazioni base per risparmiare tempo."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
