from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_podcast_radio_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast & Radio – Livello 5*\n\n"

        "Podcast professionale: intro, jingle, editing avanzato, pubblicazione su Spotify e Apple Podcast."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
