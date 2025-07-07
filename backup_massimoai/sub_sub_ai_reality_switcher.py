from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def ai_reality_switcher_handler(update, context):

    user = update.effective_user

    text = (

        "🌀 *Reality Switcher*\n\n"

        "Impara a cambiare mindset in tempo reale: scegli lo stato mentale (focus, creatività, sicurezza, energia) e ricevi esercizi, tecniche e una traccia audio personalizzata da Massimo AI."

    )

    buttons = [

        [InlineKeyboardButton("Cambia stato mentale", callback_data="switch_mindset")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

