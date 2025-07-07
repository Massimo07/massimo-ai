from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from utils import USERS

ADMIN_ID = 123456789  # Il tuo telegram ID

async async async def admin_dashboard_handler(update, context):

    user = update.effective_user

    if user.id != ADMIN_ID:

        await context.bot.send_message(chat_id=user.id, text="Non hai i permessi.")

        return

    text = (

        f"🛡️ *Admin Dashboard*\n\n"

        f"Utenti registrati: {len(USERS)}\n"

        f"Gestione abbonamenti, alert, blocco utenti."

    )

    buttons = [

        [InlineKeyboardButton("Scarica CSV utenti", callback_data="admin_csv")],

        [InlineKeyboardButton("Esporta report", callback_data="admin_report")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )
