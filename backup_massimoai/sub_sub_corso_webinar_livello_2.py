from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_webinar_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🎤 *Webinar – Livello 2*\n\n"

        "Come prepararsi per un webinar: audio, video, puntualità, domande frequenti, prendere appunti e interagire."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

