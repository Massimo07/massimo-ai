from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_avatar_ai_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🧑‍💻 *Avatar & Voice AI – Livello 7*\n\n"

        "Avatar AI evoluto: deepfake etico, avatar-clone, voce emozionale, avatar come speaker in eventi, onboarding e gestione community globale!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

