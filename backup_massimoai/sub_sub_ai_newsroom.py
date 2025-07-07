from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def ai_newsroom_handler(update, context):

    user = update.effective_user

    text = (

        "📰 *Magic Newsroom*\n\n"

        "Tutte le ultime news, aggiornamenti, nuovi prodotti e eventi in tempo reale!"

    )

    buttons = [

        [InlineKeyboardButton("Iscriviti alle notifiche", callback_data="subscribe_news")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

