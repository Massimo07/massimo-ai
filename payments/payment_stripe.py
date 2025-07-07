from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import stripe

import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from utils import get_user

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

LEVELS = [

    {"name": "Info Free", "price": 0},

    {"name": "Primo Passo", "price": 15},

    {"name": "Cambio Vita", "price": 40},

    {"name": "Mentalità Vincente", "price": 70},

    {"name": "Crescita Esponenziale", "price": 110},

    {"name": "Imprenditore Libero", "price": 160},

    {"name": "Guida del Team", "price": 220},

    {"name": "Network Leggendario", "price": 300},

]

async def payment_handler(update, context):

    user = update.effective_user

    data = get_user(user.id)

    text = (

        "💎 *Abbonati a Massimo AI*\n"

        "Scegli il tuo livello e attiva il percorso!\n"

        "(Il pagamento è sicuro e ricorrente, puoi disdire in qualsiasi momento)"

    )

    buttons = [

        [InlineKeyboardButton(f"{lvl['name']} – {lvl['price']} € / mese", callback_data=f"buy_{i}")]

        for i, lvl in enumerate(LEVELS)

    ]

    await context.bot.send_message(

        chat_id=user.id,

        text=text,

        parse_mode="Markdown",

        reply_markup=InlineKeyboardMarkup(buttons)

    )

async def buy_level_handler(update, context):

    query = update.callback_query

    user = query.from_user

    level_idx = int(query.data.replace("buy_", ""))

    level = LEVELS[level_idx]

    session = stripe.checkout.Session.create(

        payment_method_types=['card'],

        line_items=[{

            'price_data': {

                'currency': 'eur',

                'unit_amount': int(level['price']) * 100,

                'product_data': {

                    'name': f"Massimo AI – {level['name']}",

                },

            },

            'quantity': 1,

        }],

        mode='subscription',

        success_url='https://t.me/massimoai_bot?start=success',

        cancel_url='https://t.me/massimoai_bot?start=cancel',

        metadata={'telegram_user_id': user.id, 'level': level_idx}

    )

    await query.edit_message_text(

        f"🔗 Clicca qui per completare il pagamento:\n{session.url}"

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
