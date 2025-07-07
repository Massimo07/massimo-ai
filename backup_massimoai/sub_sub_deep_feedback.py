from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def deep_feedback_handler(update, context):

    user = update.effective_user

    text = (

        "🔬 *Deep Feedback*\n"

        "Analisi avanzata delle opinioni utenti, sentiment analysis, AI listening, suggerimenti evoluti. Ogni dettaglio conta!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

