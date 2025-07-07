from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_avatar_ai_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🧑‍💻 *Avatar & Voice AI – Livello 3*\n\n"

        "Carica il tuo avatar personalizzato! Animazioni base, reazioni automatiche, introduzione agli avatar parlanti nei video."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

