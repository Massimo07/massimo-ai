from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async def eventi_webinar_handler(update, context):

    user = update.effective_user

    text = (

        "📆 *Eventi & Webinar*\n\n"

        "Ecco la lista aggiornata di tutti gli eventi Magic Team Live On Plus!\n"

        "– Webinar settimanale: ogni lunedì ore 21\n"

        "– Masterclass mensile: primo sabato del mese\n"

        "Iscriviti e ricevi il link personalizzato!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
