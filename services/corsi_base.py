from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from translations import t

CORSI_BASE = [

    {"titolo": "Capire il cliente e ascolto attivo", "desc": "Impara a comprendere chi hai di fronte e ascoltare davvero i bisogni.", "step": 1},

    {"titolo": "Presentazione efficace del prodotto", "desc": "Come spiegare benefici e differenze in modo chiaro.", "step": 2},

    {"titolo": "Linguaggio del corpo", "desc": "Leggi i segnali non verbali per chiudere più vendite.", "step": 3},

    {"titolo": "Gestione delle obiezioni", "desc": "Trasforma i dubbi del cliente in opportunità.", "step": 4},

    {"titolo": "Quiz Finale", "desc": "Testa quello che hai imparato!", "step": 5}

]

async def corsi_base_handler(update, context):

    user = update.effective_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    buttons = []

    for corso in CORSI_BASE:

        buttons.append([InlineKeyboardButton(f"{corso['titolo']} [Inizia]", callback_data=f"cbase_{corso['step']}")])

    await context.bot.send_message(

        chat_id=user.id,

        text=t("corso_base_intro", lang),

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async def corso_base_step_handler(update, context):

    query = update.callback_query

    user = query.from_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    step = int(query.data.replace("cbase_", ""))

    corso = next((c for c in CORSI_BASE if c['step'] == step), None)

    if not corso:

        await query.edit_message_text(t("step_non_trovato", lang))

        return

    await query.edit_message_text(

        f"*{corso['titolo']}*\n{corso['desc']}",

        parse_mode="Markdown"

    )

    # Dopo ogni step, puoi aggiungere domande AI (es: "Vuoi una simulazione?", "Hai domande su questo step? Scrivile qui!") e rispondere col modulo massimo_ai_handler

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
