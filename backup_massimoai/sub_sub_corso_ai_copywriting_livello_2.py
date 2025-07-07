from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_ai_copywriting_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *AI Copywriting – Livello 2*\n\n"

        "Crea slogan, headline, email automatiche per clienti e team, primi template personalizzati."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

