from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from translations import t

from levels import LEVELS

def get_menu_keyboard(lang="it"):

    return InlineKeyboardMarkup([

        [InlineKeyboardButton(t("cos_e_nm", lang), callback_data="cos_e_nm")],

        [InlineKeyboardButton(t("chi_e_lop", lang), callback_data="live_on_plus")],

        [InlineKeyboardButton(t("piano_marketing", lang), callback_data="piano_marketing")],

        [InlineKeyboardButton(t("differenze", lang), callback_data="differenze")],

        [InlineKeyboardButton(t("perche_lop", lang), callback_data="vantaggi")],

        [InlineKeyboardButton(t("perche_magic_team", lang), callback_data="magic_team")],

        [InlineKeyboardButton(t("faq", lang), callback_data="faq")],

        [InlineKeyboardButton(t("motivazione_giorno", lang), callback_data="motivazione")],

        [InlineKeyboardButton(t("prodotti_cataloghi", lang), callback_data="prodotti")],

        [InlineKeyboardButton(t("registrati", lang), callback_data="registrazione")],

        [InlineKeyboardButton(t("sei_indeciso", lang), callback_data="indeciso")],

        [InlineKeyboardButton(t("momento_no", lang), callback_data="momento_no")],

        [InlineKeyboardButton(t("scarica_libro", lang), callback_data="book")],

        [InlineKeyboardButton(t("eventi_webinar", lang), callback_data="eventi")],

        [InlineKeyboardButton(t("aggiornamenti_news", lang), callback_data="news")],

        [InlineKeyboardButton(t("vendita_autoconsumo", lang), callback_data="vendita_autoconsumo")],

        [InlineKeyboardButton(t("abbonati_scopri", lang), callback_data="dashboard")]

    ])

async async async def menu_handler(update, context):

    user = update.effective_user if hasattr(update, "effective_user") else update.callback_query.from_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    name = data.get("name", t("amico", lang))

    level = data.get("level", 0)

    await context.bot.send_message(

        chat_id=user.id,

        text=f"{t('main_menu', lang)} {name}! 💎\n\n{t('current_level', lang)} {LEVELS[level]['nome']}",

        reply_markup=get_menu_keyboard(lang)

    )
