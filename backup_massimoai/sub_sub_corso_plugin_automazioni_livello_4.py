from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_plugin_automazioni_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🔌 *Plugin & Automazioni – Livello 4*\n\n"

        "Integrazioni avanzate: bot WhatsApp-Telegram, invio report automatici, gestione eventi live multicanale."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

