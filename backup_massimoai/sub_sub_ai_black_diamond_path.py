from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_black_diamond_path_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *AI Black Diamond Path*\n"

        "Il percorso definitivo verso la qualifica massima, con tappe, obiettivi, milestone, premi e strategie avanzate."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

