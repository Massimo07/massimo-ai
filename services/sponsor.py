from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def sponsor_handler(update, context):

    user = update.effective_user

    # Mostra lista sponsor (demo)

    sponsor_list = ["Massimo AI - Palermo", "Sara Bianchi - Milano", "Luca Verdi - Roma"]

    buttons = [[InlineKeyboardButton(s, callback_data=f"sponsor_{s.split()[0]}")] for s in sponsor_list]

    await context.bot.send_message(

        chat_id=user.id,

        text="Scegli il tuo sponsor dalla lista:",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
