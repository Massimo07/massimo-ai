from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

PLUGINS = [

    {"name": "AI Funnel Master", "desc": "Crea funnel automatici in 2 click."},

    {"name": "Video Resume", "desc": "Crea video curriculum AI."},

    {"name": "Smart Contracts", "desc": "Automatizza bonus e premi su blockchain."},

]

async def plugin_marketplace_handler(update, context):

    user = update.effective_user

    text = (

        "🛒 *Plugin Marketplace*\n\n"

        "Scegli plugin aggiuntivi per potenziare Massimo AI. Ogni mese nuove funzioni!"

    )

    plugin_list = "\n".join([f"- *{p['name']}*: {p['desc']}" for p in PLUGINS])

    buttons = [

        [InlineKeyboardButton("Aggiungi plugin", callback_data="add_plugin")],

        [InlineKeyboardButton("🏠 Torna Home", callback_data="home")]

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=f"{text}\n\n{plugin_list}",

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
