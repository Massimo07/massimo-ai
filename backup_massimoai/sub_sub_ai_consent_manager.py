from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def ai_consent_manager_handler(update, context):

    user = update.effective_user

    text = (

        "🔐 *Consenso e Controllo Dati*\n\n"

        "Gestisci i permessi, la privacy e decidi tu come usare i tuoi dati. Puoi anche richiedere la cancellazione immediata!"

    )

    buttons = [

        [InlineKeyboardButton("Modifica preferenze", callback_data="edit_consent")],

        [InlineKeyboardButton("Cancella tutto", callback_data="delete_all_data")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

