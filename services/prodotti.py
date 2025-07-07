from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def prodotti_handler(update, context):

    user = update.effective_user

    text = (

        "🧴 *Prodotti & Cataloghi*\n\n"

        "Chiedimi che problema vuoi risolvere, ti consiglio il prodotto migliore Live On Plus.\n"

        "Scarica il catalogo ufficiale: [PDF Catalogo](link_catalogo)\n"

        "Per ogni dubbio, Massimo AI risponde sempre!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
