from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Realtime Coach – Allenatore personale AI in tempo reale

async async async def ai_realtime_coach_handler(update, context):

    await update.callback_query.edit_message_text(

        "🏅 Massimo AI è il tuo coach personale in tempo reale: ti aiuta a prendere decisioni, preparare una presentazione, migliorare le performance e ti motiva a ogni step!"

    )
