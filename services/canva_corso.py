from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

CORSO_CANVA = [

    {"titolo": "Cos’è Canva? Interfaccia e funzioni base", "desc": "Creare un account, navigare nei template.", "step": 1},

    {"titolo": "Come creare un post accattivante", "desc": "Immagini, font, colori che convertono.", "step": 2},

    {"titolo": "Impaginazione, formati e trucchi", "desc": "Dalle stories ai reel: come ottimizzare per ogni social.", "step": 3},

    {"titolo": "Canva Pro e strumenti avanzati", "desc": "Animazioni, brand kit, team work.", "step": 4},

    {"titolo": "Quiz finale e challenge grafica", "desc": "Crea e invia il tuo post migliore, Massimo AI ti darà un feedback!", "step": 5}

]

async def canva_corso_handler(update, context):

    user = update.effective_user

    lang = get_user(user.id).get("lang", "it")

    buttons = [

        [InlineKeyboardButton(f"{corso['titolo']} [Inizia]", callback_data=f"canva_{corso['step']}")]

        for corso in CORSO_CANVA

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text="Benvenuto al corso CANVA – qui impari tutto su grafica e post efficaci!",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async def canva_step_handler(update, context):

    query = update.callback_query

    user = query.from_user

    lang = get_user(user.id).get("lang", "it")

    step = int(query.data.replace("canva_", ""))

    corso = next((c for c in CORSO_CANVA if c['step'] == step), None)

    if not corso:

        await query.edit_message_text("Step non trovato!")

        return

    await query.edit_message_text(

        f"*{corso['titolo']}*\n{corso['desc']}",

        parse_mode="Markdown"

    )

    # Hook AI: "Vuoi un esempio o simulazione AI su questo argomento? Scrivi qui!"

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
