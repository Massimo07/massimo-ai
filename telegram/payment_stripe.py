from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
# services/payment_stripe.py

# Pseudocodice: inserisci la tua chiave stripe nel .env e aggiorna qui!

import stripe, os

stripe.api_key = os.getenv("STRIPE_KEY")

def check_abbonamento(user_id):

    # Verifica pagamento, aggiorna accesso livelli

    # ... (logica API Stripe)

    pass

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
