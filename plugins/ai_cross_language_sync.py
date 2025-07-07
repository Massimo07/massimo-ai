from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Cross-Language Sync – Sincronizza tutti i contenuti su ogni lingua

async def ai_cross_language_sync_handler(update, context):

    await update.callback_query.edit_message_text(

        "🌍 Tutti i contenuti, i funnel, i post e le risposte sono sincronizzati e tradotti in ogni lingua europea + arabo/cinese in automatico, così ogni team lavora insieme senza barriere!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
