from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

import requests

def call_external_api(url, params=None):

    try:

        response = requests.get(url, params=params)

        if response.status_code == 200:

            return response.json()

        return None

    except Exception as e:

        print(f"Errore API: {e}")

        return None

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
