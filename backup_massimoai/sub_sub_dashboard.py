from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
from utils import USERS

import pandas as pd

def export_dashboard():

    df = pd.DataFrame.from_dict(USERS, orient="index")

    df.to_excel("backup/dashboard_export.xlsx")

async async async def dashboard_admin_handler(update, context):

    admin_id = 123456789  # ID Massimo, sostituire col tuo!

    if update.effective_user.id != admin_id:

        await context.bot.send_message(chat_id=update.effective_user.id, text="Non autorizzato.")

        return

    utenti = len(USERS)

    abbonati = sum(1 for u in USERS.values() if u.get("level", 0) > 0)

    await context.bot.send_message(

        chat_id=admin_id,

        text=f"Utenti totali: {utenti}\nAbbonati: {abbonati}\nEsporta dashboard da /backup"

    )
