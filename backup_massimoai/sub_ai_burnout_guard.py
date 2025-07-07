from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_burnout_guard_handler(update, context):

    user = update.effective_user

    text = (

        "🛡️ *AI Burnout Guard*\n"

        "AI che monitora stress, burnout, segnali di stanchezza. Suggerisce pause, attività benessere e reset emotivo. Salute prima di tutto!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
