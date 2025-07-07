from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_autotraining_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🧘 *Autotraining & Meditazione – Livello 2*\n\n"

        "Meditazione guidata breve: elimina lo stress, trova la calma interiore, esercizi audio per ricaricare le energie."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

