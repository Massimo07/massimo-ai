from telegram import Update
from telegram.ext import ContextTypes
from utils import USERS

async def export_utenti_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Esporta tutti gli utenti in un file CSV."""
    from io import StringIO
    import csv

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["user_id", "nome", "provincia", "lingua", "livello"])
    for user_id, data in USERS.items():
        writer.writerow([user_id, data.get("name"), data.get("province"), data.get("lang"), data.get("level")])
    output.seek(0)
    await update.callback_query.message.reply_document(document=output, filename="utenti_massimoai.csv")
