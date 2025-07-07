from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

CORSO_NM = [

    {"titolo": "Cos’è davvero il Network Marketing?", "desc": "La vera definizione, senza cliché.", "step": 1},

    {"titolo": "Approccio con i contatti: caldo, tiepido, freddo", "desc": "Come presentarti, cosa evitare.", "step": 2},

    {"titolo": "Come si spiegano azienda, piano marketing e prodotti", "desc": "Le parole giuste per ogni situazione.", "step": 3},

    {"titolo": "Obiezioni più comuni e risposte vincenti", "desc": "Anticipa i dubbi e scioglili con sicurezza.", "step": 4},

    {"titolo": "Quiz finale + simulazione con Massimo AI", "desc": "Ti mettiamo alla prova con casi reali!", "step": 5}

]

async async async def network_marketing_corso_handler(update, context):

    user = update.effective_user

    lang = get_user(user.id).get("lang", "it")

    buttons = [

        [InlineKeyboardButton(f"{corso['titolo']} [Inizia]", callback_data=f"nm_{corso['step']}")]

        for corso in CORSO_NM

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text="Il percorso completo di Network Marketing, passo dopo passo!",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async async async def network_marketing_step_handler(update, context):

    query = update.callback_query

    user = query.from_user

    lang = get_user(user.id).get("lang", "it")

    step = int(query.data.replace("nm_", ""))

    corso = next((c for c in CORSO_NM if c['step'] == step), None)

    if not corso:

        await query.edit_message_text("Step non trovato!")

        return

    await query.edit_message_text(

        f"*{corso['titolo']}*\n{corso['desc']}",

        parse_mode="Markdown"

    )

    # Ogni step può concludersi: "Vuoi una simulazione AI? Chiedi qui!"
