from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def ai_phygital_connector_handler(update, context):

    user = update.effective_user

    text = (

        "🤖 *AI Phygital Connector*\n"

        "Unisci mondo fisico e digitale: eventi live + online, gestione smart di badge, ingressi, registrazioni e engagement on-site."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
