from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def doc_generator_handler(update, context):

    user = update.effective_user

    text = (

        "📑 *Document Generator*\n\n"

        "Genera automaticamente PDF, presentazioni, slide e guide personalizzate per il tuo team o i clienti!"

    )

    buttons = [

        [InlineKeyboardButton("Crea PDF ora", callback_data="create_pdf")],

        [InlineKeyboardButton("Crea presentazione", callback_data="create_presentation")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
