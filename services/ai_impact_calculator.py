from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_impact_calculator_handler(update, context):

    user = update.effective_user

    text = (

        "🧮 *Impact Calculator*\n\n"

        "Stima l’impatto del tuo business: numeri, crescita, clienti, incasso potenziale, duplicazione! Prova simulazioni e vedi cosa cambia se porti un nuovo venditore o 10 clienti nuovi."

    )

    buttons = [

        [InlineKeyboardButton("Fai simulazione", callback_data="start_impact_calc")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
