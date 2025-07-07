from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Competitor Scanner – Analizza i concorrenti

async def ai_competitor_scanner_handler(update, context):

    await update.callback_query.edit_message_text(

        "🔎 Scansiona e monitora i siti/profili social della concorrenza: l’AI segnala novità, offerte, trend e suggerisce azioni per superarli."

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
