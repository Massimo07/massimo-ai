from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def personality_handler(update, context):

    user = update.effective_user

    text = (

        "🧬 *Personality Analyzer*\n\n"

        "Scopri il tuo stile comunicativo, i punti di forza e come migliorare le relazioni nel network marketing. Quiz interattivo e analisi personalizzata!"

    )

    buttons = [

        [InlineKeyboardButton("Fai il test ora", callback_data="start_personality_test")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
