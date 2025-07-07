from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/loyalty_engine.py

def add_loyalty_points(user_id, amount, users_db):

    if user_id not in users_db:

        users_db[user_id] = {}

    users_db[user_id]['loyalty_points'] = users_db[user_id].get('loyalty_points', 0) + amount

    # Salva su file o DB

    return users_db[user_id]['loyalty_points']

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
