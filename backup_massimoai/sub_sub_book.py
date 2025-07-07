from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

BOOK_LINK = "https://amzn.to/3SzQFqU"

async async async def book_handler(update, context):

    user = update.effective_user

    text = (

        "📖 *Scarica il Libro di Massimo*\n\n"

        "Tutta la motivazione, strategie e segreti del successo: leggilo ora!"

        f"\n\n[Scarica/Acquista qui]({BOOK_LINK})"

    )

    buttons = [

        [InlineKeyboardButton("Compra il libro", url=BOOK_LINK)],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

