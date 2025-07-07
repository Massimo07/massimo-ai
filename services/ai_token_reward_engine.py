from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Token Reward Engine – Premi digitali, token, badge NFT

async def ai_token_reward_engine_handler(update, context):

    await update.callback_query.edit_message_text(

        "🏆 Ogni sfida superata, ordine fatto o evento completato può far guadagnare token, badge NFT e premi digitali direttamente nel tuo wallet Live On Plus!"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
