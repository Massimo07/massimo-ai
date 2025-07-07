from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def abbonati_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Abbonati e Sblocca Tutto!* \n\n"

        "Scegli il livello che vuoi: ogni livello sblocca servizi, corsi, automazioni, AI esclusiva, funnel e dashboard. "

        "Clicca sul bottone e scopri tutti i vantaggi, prezzi e contenuti."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
