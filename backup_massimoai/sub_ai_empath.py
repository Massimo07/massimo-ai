from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_empath_handler(update, context):

    user = update.effective_user

    text = (

        "💗 *AI Empath*\n"

        "Supporto emotivo AI: capisce il tuo stato d’animo, ti motiva, ti ascolta, ti accompagna. Sempre presente, mai solo!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
