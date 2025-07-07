from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_podcast_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast Pro – Livello 3*\n\n"

        "Sigle, effetti audio, pubblicazione su più piattaforme, mini-serie e narrazione."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

