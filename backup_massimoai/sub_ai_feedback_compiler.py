from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Social Recruiter – Trova e prequalifica prospect da LinkedIn, IG, FB

async async async def ai_social_recruiter_handler(update, context):

    await update.callback_query.edit_message_text(

        "🔍 L’AI trova, analizza e prequalifica nuovi contatti sui social, li inserisce nel CRM, propone messaggi personalizzati per l’approccio e traccia chi risponde!"

    )
