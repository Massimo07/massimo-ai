from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def cross_network_analyzer_handler(update, context):

    user = update.effective_user

    text = (

        "🌐 *Cross-Network Analyzer*\n\n"

        "Analizza in tempo reale tutte le tue performance su Telegram, WhatsApp, LinkedIn, Facebook e Instagram.\n"

        "Scopri dove hai più risultati e come migliorare!"

    )

    buttons = [

        [InlineKeyboardButton("Analizza ora", callback_data="run_network_analysis")],

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
