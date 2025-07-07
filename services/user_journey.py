from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def user_journey_handler(update, context):

    user = update.effective_user

    text = (

        "🗺️ *User Journey Mapper*\n\n"

        "Segui ogni utente dal primo contatto all’attivazione, dal follow-up al rinnovo abbonamento. Tutto tracciato, tutto ottimizzabile!"

    )

    buttons = [

        [InlineKeyboardButton("Visualizza mappa", callback_data="show_journey")],

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
