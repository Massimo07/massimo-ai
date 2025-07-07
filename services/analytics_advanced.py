from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/analytics_advanced.py

import pandas as pd

def generate_analytics(users_data):

    df = pd.DataFrame(users_data)

    stats = {

        "active_users": df[df['active']==True].shape[0],

        "churn_rate": df[df['churned']==True].shape[0] / df.shape[0],

        # ... altri KPI personalizzati

    }

    return stats

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
