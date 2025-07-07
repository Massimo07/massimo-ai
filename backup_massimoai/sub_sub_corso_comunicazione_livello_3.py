from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_comunicazione_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🗣️ *Corso Comunicazione – Livello 3*\n\n"

        "Public speaking, gestione delle emozioni, come parlare in pubblico dal vivo e online. Allenamento pratico."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

