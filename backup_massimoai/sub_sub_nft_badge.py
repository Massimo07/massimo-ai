from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def nft_badge_handler(update, context):

    user = update.effective_user

    text = (

        "🏅 *NFT Badge*\n"

        "Ogni risultato importante diventa un NFT unico, colleziona i tuoi traguardi sulla blockchain Magic Team!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

