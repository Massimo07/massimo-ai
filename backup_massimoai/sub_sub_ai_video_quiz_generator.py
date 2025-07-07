from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Video Quiz Generator – Quiz interattivi video su prodotti, corsi, onboarding

async async async def ai_video_quiz_generator_handler(update, context):

    await update.callback_query.edit_message_text(

        "📺 Crea quiz interattivi video su prodotti, corsi e onboarding: Massimo AI premia chi risponde meglio e raccoglie i risultati in tempo reale!"

    )

