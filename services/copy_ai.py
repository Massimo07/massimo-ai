from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def copy_ai_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *Copy AI*\n"

        "Crea testi, post, headline, email, blog e contenuti funnel con AI. Scegli tono, target e obiettivo. Tutto personalizzato!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
