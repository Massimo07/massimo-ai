from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_podcast_radio_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast & Radio – Livello 4*\n\n"

        "Gestione palinsesto, programmazione contenuti, collaborazione con altri membri, dirette radio su Telegram."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

