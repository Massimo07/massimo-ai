from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI News Aggregator – Notizie, tendenze e competitor

async def ai_news_aggregator_handler(update, context):

    await update.callback_query.edit_message_text(

        "📰 AI News Aggregator ti aggiorna su novità, trend e anche attività dei competitor, così puoi anticipare il mercato e ispirare tutto il tuo team!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
