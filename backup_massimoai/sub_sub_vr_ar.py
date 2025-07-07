from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async def vr_ar_handler(update, context):

    user = update.effective_user

    text = (

        "🕶️ *VR/AR Advanced*\n\n"

        "Entra nel Metaverso Magic Team! Partecipa a meeting virtuali, formazione immersiva, simulazioni di vendita."

        "\n\nAccesso riservato ai livelli più alti e a chi completa i corsi di formazione avanzata."

    )

    buttons = [

        [InlineKeyboardButton("Accedi ora (Demo)", callback_data="enter_vr")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

