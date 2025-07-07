from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def social_manager_handler(update, context):

    user = update.effective_user

    await context.bot.send_message(

        chat_id=user.id,

        text="Questa sezione ti aiuta a creare, programmare e gestire i tuoi social come un vero professionista! Vuoi pubblicare, sponsorizzare o creare contenuti con l’AI?"

    )

    # Espandibile: collegamento API social (Facebook, Instagram, LinkedIn, TikTok, ecc.)
