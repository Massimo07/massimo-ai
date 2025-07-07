from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

MOTIVATIONAL_QUOTES = [

    "Non è mai troppo tardi per essere ciò che avresti potuto essere.",

    "Sii il cambiamento che vuoi vedere nel mondo.",

    "La strada verso il successo è sempre in costruzione.",

    "Credi in te stesso, sempre.",

]

async async async def motivator_handler(update, context):

    user = update.effective_user

    quote = random.choice(MOTIVATIONAL_QUOTES)

    text = f"✨ *Motivazione del giorno*\n\n_{quote}_"

    buttons = [

        [InlineKeyboardButton("Altra motivazione", callback_data="new_quote")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
