from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from translations import t

CRESCITA_PERSONALE = [

    {"titolo": "Scoprire il tuo perché", "desc": "Trova la tua vera motivazione.", "step": 1},

    {"titolo": "Obiettivi SMART", "desc": "Tecniche per fissare e raggiungere gli obiettivi.", "step": 2},

    {"titolo": "Gestione tempo", "desc": "Metodo pratico per aumentare la produttività.", "step": 3},

    {"titolo": "Comunicazione efficace", "desc": "Migliora i tuoi risultati parlando meglio.", "step": 4},

    {"titolo": "Quiz Finale", "desc": "Metti alla prova i tuoi progressi.", "step": 5}

]

async async async def crescita_personale_handler(update, context):

    user = update.effective_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    buttons = []

    for corso in CRESCITA_PERSONALE:

        buttons.append([InlineKeyboardButton(f"{corso['titolo']} [Inizia]", callback_data=f"crescita_{corso['step']}")])

    await context.bot.send_message(

        chat_id=user.id,

        text=t("corso_crescita_intro", lang),

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async async async def crescita_personale_step_handler(update, context):

    query = update.callback_query

    user = query.from_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    step = int(query.data.replace("crescita_", ""))

    corso = next((c for c in CRESCITA_PERSONALE if c['step'] == step), None)

    if not corso:

        await query.edit_message_text(t("step_non_trovato", lang))

        return

    await query.edit_message_text(

        f"*{corso['titolo']}*\n{corso['desc']}",

        parse_mode="Markdown"

    )

