from telegram import Update
from telegram.ext import ContextTypes
from utils import USERS

async def stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostra statistiche chiave su utenti e livelli."""
    total = len(USERS)
    by_level = {}
    for u in USERS.values():
        lvl = u.get("level", 0)
        by_level[lvl] = by_level.get(lvl, 0) + 1
    msg = f"👤 Utenti Totali: {total}\n"
    msg += "\n".join([f"• Livello {lvl}: {cnt}" for lvl, cnt in sorted(by_level.items())])
    await update.callback_query.message.reply_text(msg)
