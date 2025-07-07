from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_mentor_match_extended_handler(update, context):

    user = update.effective_user

    text = (

        "🤝 *Mentor Matching Avanzato*\n"

        "Collegamento diretto con mentor di altri team, richiesta sessione live, valutazione feedback 1-to-1, AI rating match."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
