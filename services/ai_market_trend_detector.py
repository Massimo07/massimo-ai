from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Market Trend Detector – Rileva trend e suggerisce nuove strategie

async def ai_market_trend_detector_handler(update, context):

    await update.callback_query.edit_message_text(

        "📊 Massimo AI analizza il mercato, i social, i competitor e ti avvisa subito quando c’è un nuovo trend da cavalcare — così sei sempre un passo avanti!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
