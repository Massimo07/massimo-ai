from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def qr_magic_handler(update, context):

    user = update.effective_user

    text = (

        "🔗 *QR Magic*\n\n"

        "Genera un QR Code personale per promuovere la tua attività, evento, referral o prodotto Live On Plus!"

    )

    buttons = [

        [InlineKeyboardButton("Genera QR Code", callback_data="generate_qr")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
