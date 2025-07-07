from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def magic_team_handler(update, context):

    user = update.effective_user

    text = (

        "✨ *Perché il Magic Team?*\n\n"

        "Entri in una community di persone speciali, con valori, formazione, motivazione, eventi esclusivi. Qui ognuno cresce e nessuno resta indietro!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

