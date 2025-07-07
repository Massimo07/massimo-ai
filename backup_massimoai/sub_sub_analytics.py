from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def analytics_handler(update, context):

    user = update.effective_user

    text = (

        "📈 *Analytics Avanzate* \n\n"

        "Monitoraggio in tempo reale di utenti, fatturato, performance del team, clienti attivi, retention, engagement e previsioni AI!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

