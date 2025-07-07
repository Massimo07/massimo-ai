from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Story Maker – Crea storie personalizzate e “storytelling” per social/recruiting

async async async def ai_story_maker_handler(update, context):

    await update.callback_query.edit_message_text(

        "📖 Racconta la tua storia! Massimo AI genera automaticamente racconti emozionali da pubblicare su social, sito o inviare ai prospect (anche in video!)."

    )

