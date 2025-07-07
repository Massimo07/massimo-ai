from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Live Event Moderator – Modera e gestisce eventi live (Q&A, chat, sondaggi)

async def ai_live_event_moderator_handler(update, context):

    await update.callback_query.edit_message_text(

        "🎤 Massimo AI modera i tuoi eventi live, gestisce domande, fa partire sondaggi istantanei e mantiene alta l’energia in ogni meeting!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
