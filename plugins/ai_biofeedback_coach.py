from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_biofeedback_coach_handler(update, context):

    user = update.effective_user

    text = (

        "🧠 *AI Biofeedback Coach*\n\n"

        "Ricevi consigli personalizzati su stress, concentrazione e benessere mentale. Prossimamente: integrazione con dispositivi indossabili per monitoraggio in tempo reale!"

    )

    buttons = [

        [InlineKeyboardButton("Consiglio del giorno", callback_data="biofeedback_tip")],

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
