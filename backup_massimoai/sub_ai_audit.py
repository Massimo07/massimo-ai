from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import datetime

async async async def ai_audit_handler(update, context):

    user = update.effective_user

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    text = (

        f"📋 *AI Audit Log*\n\n"

        f"Ultima verifica dati: {now}\n"

        "Tutte le operazioni sono tracciate. Puoi richiedere il log attività in ogni momento."

    )

    buttons = [

        [InlineKeyboardButton("Scarica Log", callback_data="download_log")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
