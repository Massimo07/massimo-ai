from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def consigli_handler(update, context):

    user = update.effective_user

    text = (

        "🧠 *Consigli personalizzati* \n"

        "Chiedi a Massimo AI qualsiasi cosa su network marketing, Live On Plus, business, crescita personale: ricevi strategie personalizzate su misura!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
