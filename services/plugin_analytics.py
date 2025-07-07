from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def plugin_analytics_handler(update, context):

    user = update.effective_user

    await context.bot.send_message(

        chat_id=user.id,

        text="Questo modulo ti offre l’analisi predittiva sui tuoi risultati di vendita e crescita!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
