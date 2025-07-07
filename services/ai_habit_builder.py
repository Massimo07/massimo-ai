from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_habit_builder_handler(update, context):

    user = update.effective_user

    text = (

        "🔁 *Habit Builder*\n\n"

        "Costruisci abitudini di successo: scegli un obiettivo (es: prospecting ogni giorno, follow-up, lettura), ricevi reminder AI, tracciamento e premi quando lo mantieni!"

    )

    buttons = [

        [InlineKeyboardButton("Imposta nuova abitudine", callback_data="set_habit")],

        [InlineKeyboardButton("Visualizza progressi", callback_data="view_habits")],

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
