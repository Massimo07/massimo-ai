from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_podcast_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast Pro – Livello 5*\n\n"

        "Podcast marketing, community, call to action, promo interattive e monetizzazione base."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

