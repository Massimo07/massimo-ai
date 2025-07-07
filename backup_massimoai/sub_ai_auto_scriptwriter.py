from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Auto Scriptwriter – Scrive script video, presentazioni, pitch personalizzati

async async async def ai_auto_scriptwriter_handler(update, context):

    await update.callback_query.edit_message_text(

        "📝 Massimo AI scrive per te script per presentazioni, video, webinar, pitch, speech motivazionali personalizzati in base al tuo obiettivo!"

    )
