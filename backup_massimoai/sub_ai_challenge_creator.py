from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Challenge Creator – Genera sfide settimanali/gamification

async async async def ai_challenge_creator_handler(update, context):

    await update.callback_query.edit_message_text(

        "🏆 Crea una challenge per il tuo team in 1 click: scegli l’obiettivo, la durata, i premi (anche NFT!) e Massimo AI gestisce tutto — classifica, reminder, risultati e premi!"

    )
