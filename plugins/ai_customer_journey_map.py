from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Customer Journey Map – Mappa il percorso utente e suggerisce ottimizzazioni

async def ai_customer_journey_map_handler(update, context):

    await update.callback_query.edit_message_text(

        "🗺️ L’AI traccia il percorso di ogni utente dalla registrazione all’acquisto, ti segnala punti deboli e suggerisce come aumentare conversioni e retention!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
