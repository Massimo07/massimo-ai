from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def talent_finder_handler(update, context):

    user = update.effective_user

    text = (

        "🔍 *Talent Finder*\n\n"

        "Scova i migliori talenti per il tuo team! Compila il profilo ideale, l’AI seleziona le persone più adatte nella community."

        "\n\nProssimamente: matching automatico anche da LinkedIn, social e community."

    )

    buttons = [

        [InlineKeyboardButton("Crea profilo ideale", callback_data="new_profile")],

        [InlineKeyboardButton("Vedi proposte AI", callback_data="show_matches")],

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
