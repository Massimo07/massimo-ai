from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def legal_guardian_handler(update, context):

    user = update.effective_user

    text = (

        "📜 *Legal & Consenso GDPR*\n\n"

        "Tutti i dati sono trattati secondo la normativa europea GDPR. Puoi scaricare i tuoi dati, modificare preferenze o cancellare il profilo in ogni momento."

    )

    buttons = [

        [InlineKeyboardButton("Scarica dati", callback_data="download_gdpr")],

        [InlineKeyboardButton("Cancella profilo", callback_data="delete_account")],

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
