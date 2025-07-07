from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def ai_generative_campaign_handler(update, context):

    user = update.effective_user

    text = (

        "🔄 *AI Generative Campaign*\n"

        "Campagne social, recruiting, eventi, email, tutto generato e ottimizzato da AI. Un solo click, risultati infiniti."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
