from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/superadmin.py

async def superadmin_handler(update, context):

    # Esempio base di pannello comandi Telegram

    keyboard = [

        [("📝 Esporta utenti", "export_users")],

        [("✅ Attiva/Disattiva utente", "toggle_user")],

        [("💰 Gestisci abbonamenti", "manage_subs")],

        [("🚦 Log accessi", "log_access")]

    ]

    # ... implementa il menu e le funzioni

    await await update.message.reply_text("Pannello SuperAdmin – scegli un’azione.")

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
