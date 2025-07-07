from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TRAINING_AREAS = [

    "Vendita base", "Obiezioni", "Time Management", "Prodotti", "Network", "Gestione Team", "Mindset", "Prospecting"

]

async def ai_trainer_handler(update, context):

    user = update.effective_user

    text = (

        "🏋️ *AI Trainer PRO*\n\n"

        "Scegli l’area che vuoi potenziare oggi e ricevi un training interattivo, step-by-step, con esercizi e quiz personalizzati."

        "\n\nAree disponibili:\n" +

        "\n".join([f"- {a}" for a in TRAINING_AREAS])

    )

    buttons = [

        [InlineKeyboardButton("Inizia Training", callback_data="start_training")],

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
