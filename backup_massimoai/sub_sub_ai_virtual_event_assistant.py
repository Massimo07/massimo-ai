from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_virtual_event_assistant_handler(update, context):

    user = update.effective_user

    text = (

        "🎤 *AI Virtual Event Assistant*\n"

        "Gestione eventi virtuali, webinar, formazione live, interazione in tempo reale, domande e risposte AI."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

