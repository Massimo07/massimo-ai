from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def scam_detector_handler(update, context):

    user = update.effective_user

    text = (

        "🛡️ *Scam Detector*\n\n"

        "Tutti i contatti e transazioni vengono verificati automaticamente dall’AI per prevenire truffe e attività sospette.\n"

        "Se noti qualcosa di strano, segnalalo qui!"

    )

    buttons = [

        [InlineKeyboardButton("Segnala sospetto", callback_data="report_scam")],

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
