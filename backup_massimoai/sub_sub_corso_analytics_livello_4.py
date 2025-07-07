from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_analytics_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "📊 *Analytics – Livello 4*\n\n"

        "Dashboard live, filtri personalizzati, monitoraggio team, andamento campagne social e vendite prodotto."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

