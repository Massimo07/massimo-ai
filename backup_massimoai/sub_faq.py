from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def faq_handler(update, context):

    user = update.effective_user

    text = (

        "❓ *FAQ* \n"

        "- Come ci si registra?\n"

        "- Come si ordina?\n"

        "- Come scegliere sponsor?\n"

        "- Quali sono i vantaggi?\n"

        "Scrivimi qualsiasi domanda: Massimo AI risponde sempre!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
