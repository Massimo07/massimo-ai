from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/referral_system.py

def assign_referral_to_user(user_id, sponsor_id):

    users = load_all_users()

    users[str(user_id)]["sponsor_id"] = sponsor_id

    # Aggiorna sponsor, salva nel file o DB

    # ...

    return True

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
