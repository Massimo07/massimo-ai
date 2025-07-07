from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
from flask import Flask, request

import stripe

import os

app = Flask(__name__)

endpoint_secret = os.getenv("STRIPE_ENDPOINT_SECRET")

@app.route('/stripe-webhook', methods=['POST'])

def stripe_webhook():

    payload = request.data

    sig_header = request.headers['STRIPE_SIGNATURE']

    event = None

    try:

        event = stripe.Webhook.construct_event(

            payload, sig_header, endpoint_secret

        )

    except Exception as e:

        print("Webhook error:", e)

        return "fail", 400

    if event['type'] == 'invoice.payment_succeeded':

        customer_id = event['data']['object']['customer']

        # Qui aggiorna il database e sblocca i servizi

        print(f"Pagamento ricorrente ok: {customer_id}")

    elif event['type'] == 'customer.subscription.deleted':

        customer_id = event['data']['object']['customer']

        # Qui blocca l’accesso

        print(f"Abbonamento annullato: {customer_id}")

    return "ok", 200

