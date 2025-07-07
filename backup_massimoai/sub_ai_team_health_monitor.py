from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Team Health Monitor – Monitora lo stato di salute/motivazione della rete

async async async def ai_team_health_monitor_handler(update, context):

    await update.callback_query.edit_message_text(

        "💡 Massimo AI monitora costantemente la motivazione e il benessere del tuo team. Ricevi alert quando qualcuno è in difficoltà e suggerimenti per rafforzare il gruppo!"

    )
