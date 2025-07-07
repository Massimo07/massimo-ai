from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def ai_magic_vision_handler(update, context):

    user = update.effective_user

    text = (

        "🌟 *Magic Vision Board 3D*\n\n"

        "Crea la tua Vision Board 3D, carica obiettivi, immagini, audio e mantra personali. Rivedila ogni giorno e ricevi ispirazione e reminder da Massimo AI!"

    )

    buttons = [

        [InlineKeyboardButton("Crea Vision Board", callback_data="create_vision_board")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

