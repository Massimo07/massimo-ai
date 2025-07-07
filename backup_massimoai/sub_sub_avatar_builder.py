from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def avatar_builder_handler(update, context):

    user = update.effective_user

    text = (

        "🧑‍🎤 *Avatar Builder*\n\n"

        "Crea e personalizza il tuo avatar AI per rappresentarti online, sui social e nelle presentazioni Magic Team!"

    )

    buttons = [

        [InlineKeyboardButton("Crea Avatar", callback_data="create_avatar")],

        [InlineKeyboardButton("Scegli voce", callback_data="choose_voice")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

