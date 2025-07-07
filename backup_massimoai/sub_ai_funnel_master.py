from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def ai_funnel_master_handler(update, context):

    user = update.effective_user

    text = (

        "🌀 *AI Funnel Master*\n\n"

        "Crea, gestisci e automatizza funnel di iscrizione, vendita, onboarding, abbonamento e follow-up in pochi click. Personalizza ogni fase, tracciamento e A/B testing AI-driven!"

    )

    buttons = [

        [InlineKeyboardButton("Crea nuovo funnel", callback_data="create_funnel")],

        [InlineKeyboardButton("Vedi performance", callback_data="show_funnel_stats")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
