from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def ai_future_proof_handler(update, context):

    user = update.effective_user

    text = (

        "🔮 *AI Future Proof*\n"

        "Analisi tendenze, scenari futuri, suggerimenti su come restare al top e anticipare tutti i cambiamenti del mercato!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
