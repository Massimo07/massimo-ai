from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_avatar_ai_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🧑‍💻 *Avatar & Voice AI – Livello 1*\n\n"

        "Cos’è un avatar digitale? Scegli il tuo avatar base per l’esperienza Massimo AI. Impara a usare la sintesi vocale semplice."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

