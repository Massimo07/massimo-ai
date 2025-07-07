from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Lead Scoring – Valutazione automatica dei lead/prospect

async def ai_lead_scoring_handler(update, context):

    await update.callback_query.edit_message_text(

        "📈 L’AI valuta e assegna un punteggio a ogni lead/prospect, così sai chi contattare prima e quali strategie usare per massimizzare i risultati!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
