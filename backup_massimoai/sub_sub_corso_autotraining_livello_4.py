from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_autotraining_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🧘 *Autotraining & Meditazione – Livello 4*\n\n"

        "Routine autotraining per il successo: tecniche di auto-ancoraggio, reset mentale e mindfulness per affrontare le sfide."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

