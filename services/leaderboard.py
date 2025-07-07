from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

LEADERS = [

    {"name": "Anna R.", "points": 1850},

    {"name": "Luigi M.", "points": 1720},

    {"name": "Sofia B.", "points": 1690},

]

async def leaderboard_handler(update, context):

    user = update.effective_user

    text = (

        "🏆 *Classifica Magic Team*\n\n" +

        "\n".join([f"{i+1}. *{l['name']}*: {l['points']} punti" for i, l in enumerate(LEADERS)]) +

        "\n\nPartecipa alle challenge per salire in classifica!"

    )

    buttons = [

        [InlineKeyboardButton("Challenge settimanali", callback_data="challenge")],

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
