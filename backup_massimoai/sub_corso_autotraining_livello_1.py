from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_autotraining_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🧘 *Autotraining & Meditazione – Livello 1*\n\n"

        "Cos’è l’autotraining? Scopri i primi esercizi di respirazione per rilassarti e aumentare concentrazione prima di ogni chiamata o presentazione."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
