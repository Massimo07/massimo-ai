from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/disaster_recovery.py

import shutil

import datetime

def backup_data(src_folder, backup_folder):

    today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    dest = os.path.join(backup_folder, f"backup_{today}")

    shutil.copytree(src_folder, dest)

    return dest

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
