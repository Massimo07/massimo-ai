from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_meta_recruiter_handler(update, context):

    user = update.effective_user

    text = (

        "🤖 *Meta Recruiter*\n\n"

        "L’AI cerca, filtra e propone nuovi candidati su tutti i social (LinkedIn, Instagram, Facebook). Valuta chi è pronto per il network e invia inviti smart, sempre in modo etico e conforme GDPR."

    )

    buttons = [

        [InlineKeyboardButton("Trova nuovi candidati", callback_data="find_candidates")],

        [InlineKeyboardButton("Imposta filtro target", callback_data="set_target")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_multiverse_portal_handler(update, context):

    user = update.effective_user

    text = (

        "🪐 *AI Multiverse Portal*\n\n"

        "Accedi a tutti i servizi Magic Team, formazione, dashboard, streaming, gamification e premi, in un’unica interfaccia!"

    )

    buttons = [

        [InlineKeyboardButton("Vai al Portale", callback_data="go_portal")],

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
