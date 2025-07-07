from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def quiz_module_handler(update, context):

    user = update.effective_user

    text = (

        "❓ *Quiz Interattivi*\n"

        "Metti alla prova le tue competenze: quiz su prodotti, marketing, crescita personale. Ogni quiz è un passo verso l’eccellenza!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
