from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Webinar Synth – Registra, trascrive e riassume webinar/eventi

async def ai_webinar_synth_handler(update, context):

    await update.callback_query.edit_message_text(

        "🎬 Registra e trascrivi qualsiasi webinar/evento live. Ottieni subito la sintesi testuale, le 10 idee chiave e i punti azione generati dall’AI per la tua rete!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
