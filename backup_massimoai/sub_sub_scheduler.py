from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def scheduler_handler(update, context):

    user = update.effective_user

    text = (

        "🗓️ *Scheduler*\n"

        "Programma meeting, appuntamenti, promemoria automatici per te e per il team. Massimo AI non si dimentica mai nulla!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

