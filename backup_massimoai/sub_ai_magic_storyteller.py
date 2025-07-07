from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_magic_storyteller_pro_handler(update, context):

    user = update.effective_user

    text = (

        "📖 *AI Storyteller Pro*\n"

        "Crea storie emozionali per ogni occasione, personalizza narrazioni per team, clienti, eventi, social. Un vero copywriter AI."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
