from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_magic_manifesto_handler(update, context):

    user = update.effective_user

    text = (

        "🪄 *AI Magic Manifesto*\n"

        "Il tuo manifesto di crescita: valori, mission, visione e regole del Magic Team, sempre a portata di mano."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

