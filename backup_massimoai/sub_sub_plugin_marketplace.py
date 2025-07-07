from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def plugin_marketplace_handler(update, context):

    user = update.effective_user

    text = (

        "🧩 *Plugin Marketplace*\n"

        "Aggiungi nuove funzioni, strumenti, automazioni, funnel e app di terze parti. Marketplace in continua evoluzione!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

