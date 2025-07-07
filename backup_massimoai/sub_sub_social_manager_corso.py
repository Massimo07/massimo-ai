from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from translations import t

CORSO_SOCIAL = [

    {"titolo": "Introduzione al Social Media Management", "desc": "Cosa fa un SMM, perché serve in ogni business.", "step": 1},

    {"titolo": "Come si crea un profilo efficace", "desc": "Strategie per Facebook, Instagram, LinkedIn e TikTok.", "step": 2},

    {"titolo": "Piano editoriale e strumenti", "desc": "Calendari, tool gratuiti, programmazione post.", "step": 3},

    {"titolo": "Sponsorizzate: principi base", "desc": "Impostare una promozione efficace senza sprecare budget.", "step": 4},

    {"titolo": "Quiz pratico", "desc": "Metti alla prova quello che hai imparato!", "step": 5}

]

async async async def social_manager_corso_handler(update, context):

    user = update.effective_user

    lang = get_user(user.id).get("lang", "it")

    buttons = [

        [InlineKeyboardButton(f"{corso['titolo']} [Inizia]", callback_data=f"smm_{corso['step']}")]

        for corso in CORSO_SOCIAL

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=t("corso_social_intro", lang),

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async async async def social_manager_step_handler(update, context):

    query = update.callback_query

    user = query.from_user

    lang = get_user(user.id).get("lang", "it")

    step = int(query.data.replace("smm_", ""))

    corso = next((c for c in CORSO_SOCIAL if c['step'] == step), None)

    if not corso:

        await query.edit_message_text(t("step_non_trovato", lang))

        return

    await query.edit_message_text(

        f"*{corso['titolo']}*\n{corso['desc']}",

        parse_mode="Markdown"

    )

    # Hook: "Hai domande o vuoi una simulazione AI? Scrivi qui!"

