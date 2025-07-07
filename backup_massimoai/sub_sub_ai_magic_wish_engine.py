from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_magic_wish_engine_handler(update, context):

    user = update.effective_user

    text = (

        "🪄 *AI Magic Wish Engine*\n"

        "Esprimi un desiderio: il motore AI lo trasforma in micro-obiettivi e piani d’azione per realizzarlo!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

