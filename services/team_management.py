from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def team_management_handler(update, context):

    user = update.effective_user

    text = (

        "🤝 *Team Management*\n"

        "Gestisci team, ruoli, onboarding nuovi membri, formazione dedicata e monitoraggio avanzamento di tutti i collaboratori!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
