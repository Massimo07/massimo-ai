from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_webinar_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🎤 *Webinar – Livello 3*\n\n"

        "Primi passi per parlare in pubblico online: come fare una presentazione breve, come gestire le emozioni e rispondere alle domande."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

