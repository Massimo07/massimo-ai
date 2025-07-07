from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_avatar_universe_handler(update, context):

    user = update.effective_user

    text = (

        "👤 *AI Avatar Universe*\n"

        "Crea, personalizza e anima il tuo avatar AI: scegli aspetto, voce, lingua, espressioni e background! Un’esperienza immersiva."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
