from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_inbox_handler(update, context):

    user = update.effective_user

    text = (

        "📥 *AI Inbox*\n"

        "Gestione messaggi, richieste, contatti inbound, risposte automatiche smart, classificazione priorità. Inbox zero garantita!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
