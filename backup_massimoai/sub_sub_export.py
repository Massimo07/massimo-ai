from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def export_handler(update, context):

    user = update.effective_user

    text = (

        "📤 *Export dati & report*\n"

        "Scarica report PDF/Excel con dati iscrizioni, clienti, risultati, avanzamenti, attività team!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

