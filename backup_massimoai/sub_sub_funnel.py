from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def funnel_handler(update, context):

    user = update.effective_user

    text = (

        "🛣️ *Funnel & Landing Page*\n"

        "Crea, modifica e automatizza funnel personalizzati: ogni step è ottimizzato per la crescita, la lead generation e il reclutamento!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

