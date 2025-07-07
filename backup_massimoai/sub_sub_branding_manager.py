from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def branding_manager_handler(update, context):

    user = update.effective_user

    text = (

        "🏷️ *Custom Branding*\n\n"

        "Personalizza la tua immagine, logo, copertine social e template per differenziarti sul mercato! Upload e preview in tempo reale."

    )

    buttons = [

        [InlineKeyboardButton("Carica nuovo logo", callback_data="upload_logo")],

        [InlineKeyboardButton("Personalizza copertina", callback_data="custom_cover")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

