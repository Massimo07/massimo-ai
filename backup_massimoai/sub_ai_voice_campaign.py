from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Voice Campaign – Campagne vocali WhatsApp/TG

async async async def ai_voice_campaign_handler(update, context):

    await update.callback_query.edit_message_text(

        "🎙️ Lancia una campagna vocale istantanea ai tuoi iscritti/prospect: Massimo AI invia, monitora chi ascolta, trascrive e risponde in automatico in ogni lingua."

    )
