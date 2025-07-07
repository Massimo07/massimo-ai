from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import random

CELEBRATION_MESSAGES = [

    "🎉 Complimenti, hai raggiunto un nuovo traguardo! Il Magic Team festeggia con te.",

    "🥳 Hai superato una sfida! Nuovo badge sbloccato.",

    "🏆 Ogni passo avanti è un successo. Continua così!",

]

async def ai_celebration_engine_handler(update, context):

    user = update.effective_user

    text = random.choice(CELEBRATION_MESSAGES)

    buttons = [

        [InlineKeyboardButton("Vedi premi & badge", callback_data="show_rewards")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=f"{text}\n\nOgni tuo risultato conta davvero nel Magic Team.",

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
