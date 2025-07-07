from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_relationship_builder_handler(update, context):

    user = update.effective_user

    text = (

        "💬 *Relationship Builder*\n\n"

        "Migliora le tue relazioni con clienti e team! Ricevi consigli su empatia, comunicazione, ascolto attivo, gestione crisi e costruisci rapporti solidi e di fiducia."

    )

    buttons = [

        [InlineKeyboardButton("Consiglio ora", callback_data="get_relationship_tip")],

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
