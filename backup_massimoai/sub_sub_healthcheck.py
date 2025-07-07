from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/healthcheck.py

import requests

def check_bot_status(telegram_token):

    url = f"https://api.telegram.org/bot{telegram_token}/getMe"

    resp = requests.get(url)

    return resp.ok

