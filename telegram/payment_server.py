# payment_server.py
import os
import stripe
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

# Mappa price_id <-> livello
LEVEL_PRICES = {
    "price_1RXqw2GsG0e6XSfX5pBwxaQZ": 1,
    "price_1RXqw4GsG0e6XSfXYLFsDFmI": 2,
    "price_1RXqw5GsG0e6XSfX988zLPiB": 3,
    "price_1RXqw6GsG0e6XSfXrVHQl676": 4,
    "price_1RXqw7GsG0e6XSfXAtmAqUye": 5,
    "price_1RXqw8GsG0e6XSfXJGI3GIkp": 6,
    "price_1RXqwAGsG0e6XSfXOYofiQ6K": 7
}

# Simula un “database” utenti
USER_UPGRADE_FILE = "pending_upgrades.json"

def load_upgrades():
    import json
    try:
        with open(USER_UPGRADE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_upgrades(data):
    import json
    with open(USER_UPGRADE_FILE, "w") as f:
        json.dump(data, f)

app = Flask(_name_)

@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.data
    sig_header = request.headers.get("stripe-signature")
    event = None
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session.get("customer_email")
        price_id = session["metadata"].get("price_id")
        telegram_id = session["metadata"].get("telegram_id")
        level = LEVEL_PRICES.get(price_id)
        # Registra upgrade in un file (sarà letto dal bot Telegram ogni 5s)
        if telegram_id and level:
            upgrades = load_upgrades()
            upgrades[telegram_id] = level
            save_upgrades(upgrades)
            print(f"[OK] Upgrade richiesto per utente Telegram {telegram_id} -> livello {level}")
    return jsonify({"status": "ok"})

if _name_ == "_main_":
    app.run(port=4242, debug=True)