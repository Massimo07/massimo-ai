from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def ai_voice_of_team_handler(update, context):

    user = update.effective_user

    text = (

        "🔊 *Voice of Team*\n\n"

        "Ricevi messaggi vocali motivazionali, di aggiornamento, feedback e storie di successo direttamente dal Magic Team, ogni giorno o ogni settimana!"

    )

    buttons = [

        [InlineKeyboardButton("Ricevi audio", callback_data="get_voice_msg")],

        [InlineKeyboardButton("Condividi storia", callback_data="share_story")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

