from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_plugin_automazioni_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🔌 *Plugin & Automazioni – Livello 5*\n\n"

        "Plugin personalizzati, API Live On Plus, export dati, sincronizzazione automatica campagne ADV."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

