from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

EVENTS = [

    {"name": "Webinar Internazionale", "date": "15 Luglio 2025"},

    {"name": "Training Live Palermo", "date": "22 Luglio 2025"},

    {"name": "Masterclass Social Selling", "date": "29 Luglio 2025"},

]

async async async def event_manager_handler(update, context):

    user = update.effective_user

    text = (

        "📆 *Eventi & Webinar*\n\n"

        "Ecco i prossimi appuntamenti live e online:\n" +

        "\n".join([f"- *{e['name']}*: {e['date']}" for e in EVENTS]) +

        "\n\nVuoi prenotarti o ricevere promemoria?"

    )

    buttons = [

        [InlineKeyboardButton("Prenota evento", callback_data="book_event")],

        [InlineKeyboardButton("Ricevi promemoria", callback_data="event_reminder")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
