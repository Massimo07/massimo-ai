from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def ai_magic_influencer_handler(update, context):

    user = update.effective_user

    text = (

        "📱 *AI Magic Influencer*\n"

        "Crea il tuo personal brand, diventa influencer nel tuo settore, strumenti AI per contenuti, storie, post e engagement."

    )

    await context.bot.send_message(chat_id=user.id, text=text)
