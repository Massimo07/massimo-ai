from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_plugin_automazioni_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🔌 *Plugin & Automazioni – Livello 3*\n\n"

        "Automatizza follow-up email, sincronizza contatti tra social e CRM, prime regole Zapier."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

