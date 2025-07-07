from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_copywriting_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *Copywriting – Livello 5*\n\n"

        "Copywriting per landing page e funnel: come scrivere una pagina che converte e un funnel automatizzato Live On Plus."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

