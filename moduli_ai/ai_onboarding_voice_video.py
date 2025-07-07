from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI Onboarding Voice+Video – Percorso onboarding vocale e video animato

async def ai_onboarding_voice_video_handler(update, context):

    await update.callback_query.edit_message_text(

        "👋 Benvenuto con la voce di Massimo AI! Onboarding guidato con video personalizzati, avatar uomo/donna a scelta, accesso rapido a tutte le funzioni di partenza."

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
