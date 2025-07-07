from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_analytics_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "📊 *Analytics – Livello 3*\n\n"

        "KPI base: tasso conversione, abbandono, PV gruppo. Report PDF mensili e alert automatici di crescita."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
