from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_avatar_ai_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🧑‍💻 *Avatar & Voice AI – Livello 5*\n\n"

        "Avatar video interattivi: inserisci emozioni, cambia espressioni, registra messaggi animati per clienti e team."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

