import os
from flask import Flask, request, abort
import stripe
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

# Simula DB utenti (integra con il tuo sistema reale)
USERS = {}

@app.route("/stripe-webhook", methods=["POST"])
def webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except (ValueError, stripe.error.SignatureVerificationError):
        abort(400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        user_id = int(session['metadata']['user_id'])
        level = int(session['metadata']['level'])

        USERS[user_id] = {'level': level, 'paid': True}
        print(f"Pagamento confermato per user {user_id} livello {level}")

        # Puoi aggiungere notifica Telegram/admin qui

    return '', 200

if __name__ == "__main__":
    app.run(port=4242)
