from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async def web_push_handler(update, context):

    user = update.effective_user

    text = (

        "🌐 *Web Push Notification*\n"

        "Ricevi aggiornamenti direttamente su desktop, browser, app mobile e Telegram. Massima reattività, ovunque tu sia!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
