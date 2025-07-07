from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI API Plugin Manager – Collega plugin esterni e API

async async async def ai_api_plugin_manager_handler(update, context):

    await update.callback_query.edit_message_text(

        "🔌 Collega qualsiasi plugin o API esterna (Google Sheets, Zapier, Stripe, Canva...) direttamente dentro Massimo AI. Ogni livello può avere plugin diversi!"

    )
