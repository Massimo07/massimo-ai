from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ar_trainer_handler(update, context):

    user = update.effective_user

    text = (

        "🕶️ *AR/VR Training*\n\n"

        "Partecipa a sessioni di formazione immersiva con realtà aumentata e virtuale!\n"

        "Prossimamente potrai simulare presentazioni, colloqui, meeting e vendita in VR/AR.\n"

        "Disponibile per abbonati dei livelli superiori."

    )

    buttons = [

        [InlineKeyboardButton("Prenota una sessione demo", callback_data="ar_vr_demo")],

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
