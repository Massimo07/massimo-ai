from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def backup_restore_handler(update, context):

    user = update.effective_user

    text = (

        "🗂️ *Backup & Restore* \n"

        "Salva sempre i tuoi dati, utenti, conversazioni, corsi, funnel e report in cloud, massima sicurezza e recupero istantaneo!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)
