from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async async async def ai_network_genome_handler(update, context):

    user = update.effective_user

    text = (

        "🧬 *Network Genome*\n\n"

        "Mappa la tua rete come il DNA! Visualizza i collegamenti, i nodi forti, chi ha più impatto e dove puntare per massimizzare la crescita."

    )

    buttons = [

        [InlineKeyboardButton("Mappa la rete", callback_data="map_network")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

