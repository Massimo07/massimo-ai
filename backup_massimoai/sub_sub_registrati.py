from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def registrati_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *Registrati* \n"

        "Inserisci nome, cognome, telefono, città e provincia.\n"

        "Poi scegli il tuo sponsor tra quelli disponibili. "

        "Se sei già iscritto a Live On Plus, inserisci il codice LOP. Altrimenti ricevi subito il referral!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

