from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def avatar_handler(update, context):

    user = update.effective_user

    text = (

        "🧑‍🚀 *Avatar AI* \n"

        "Scegli il tuo avatar personalizzato (uomo/donna/AI). Attiva sintesi vocale, modifica aspetto, scegli stile, emozioni e lingua della voce."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

