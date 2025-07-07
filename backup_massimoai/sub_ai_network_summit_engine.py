from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_network_summit_engine_handler(update, context):

    user = update.effective_user

    text = (

        "🏛️ *AI Network Summit Engine*\n"

        "Organizza, pianifica e vivi eventi digitali, summit, convention online, tavole rotonde AI-powered. Coinvolgimento massimo!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
