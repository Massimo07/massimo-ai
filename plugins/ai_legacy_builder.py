from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_ultra_analytics_handler(update, context):

    user = update.effective_user

    text = (

        "📈 *Ultra Analytics*\n\n"

        "Analisi predittiva, dati live, comparazione tra collaboratori, alert automatici sulle migliori strategie. Ricevi report settimanali e suggerimenti AI su dove puntare per crescere!"

    )

    buttons = [

        [InlineKeyboardButton("Vedi analytics", callback_data="show_analytics")],

        [InlineKeyboardButton("Ricevi report settimanale", callback_data="send_report")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_legacy_builder_handler(update, context):

    user = update.effective_user

    text = (

        "🌱 *Legacy Builder*\n\n"

        "Costruisci la tua eredità: storie, video, audio, tutorial, ebook personalizzati che restano per sempre nel Magic Team e nella tua community. Crea un impatto duraturo!"

    )

    buttons = [

        [InlineKeyboardButton("Crea legacy", callback_data="create_legacy")],

        [InlineKeyboardButton("Condividi con il team", callback_data="share_legacy")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
