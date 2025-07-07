from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_webinar_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🎤 *Webinar Base – Livello 1*\n\n"

        "Cos’è un webinar, perché è utile e come partecipare per la prima volta. Primi consigli per ascoltare e fare domande."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

