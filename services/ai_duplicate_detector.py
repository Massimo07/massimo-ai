from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Duplicate Detector – Rileva e gestisce doppioni/profili fake nel team

async def ai_duplicate_detector_handler(update, context):

    await update.callback_query.edit_message_text(

        "🔍 Massimo AI analizza i dati del team per trovare profili duplicati, fake o iscrizioni sospette. Zero sprechi, massima efficienza!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
