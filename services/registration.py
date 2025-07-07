from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from translations import t

async def registration_handler(update, context):

    user = update.effective_user if hasattr(update, "effective_user") else update.callback_query.from_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    # Step 1: Nome, Cognome, Cell, Città, Provincia

    await context.bot.send_message(

        chat_id=user.id,

        text=t("registration_intro", lang)

    )

    # (Qui puoi guidare l'utente con domande sequenziali e salvataggio progressivo nel file /data/users.json)

    # Step 2: Scelta sponsor (da file /data/sponsor.csv filtrato per città/provincia/nome/cognome)

    # Step 3: Bottone "Sono già iscritto in Live On Plus" vs "Registrati in Live On Plus"

    # Step 4: Inserimento codice LOP, alert a Massimo, verifica automatica/umana

    # Placeholder, vedi modulo completo di funnel per logica avanzata

    await context.bot.send_message(

        chat_id=user.id,

        text="Registrazione completata! Riceverai istruzioni per completare l’accesso in Live On Plus e accedere ai corsi base di vendita."

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
