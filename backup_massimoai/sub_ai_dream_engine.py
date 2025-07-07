from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def ai_dream_engine_handler(update, context):

    user = update.effective_user

    text = (

        "💭 *AI Dream Engine*\n\n"

        "Scrivi, visualizza e realizza i tuoi sogni personali e professionali. L’AI ti guida ogni giorno nel percorso per raggiungerli, con consigli, immagini, playlist motivazionali e task automatici."

    )

    buttons = [

        [InlineKeyboardButton("Scrivi sogno", callback_data="write_dream")],

        [InlineKeyboardButton("Visualizza dream board", callback_data="show_dreamboard")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
