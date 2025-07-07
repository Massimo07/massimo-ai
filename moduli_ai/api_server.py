"""
Modulo: api_server.py
Server API REST per Massimo AI: esporta dati, integra CRM esterni, riceve webhook, permette automazioni e dashboard avanzate.
Pronto per Flask/FastAPI. Sicurezza con API key/token.
"""

from flask import Flask, request, jsonify
import data_manager
import feedback

app = Flask(__name__)

API_KEY = "TUO_API_KEY_SUPER_SECRET"  # Da .env per sicurezza

def check_api_key():
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        return False
    return True

@app.route("/users", methods=["GET"])
def get_users():
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(data_manager.get_all_users())

@app.route("/feedback", methods=["GET"])
def get_feedback():
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(feedback.get_feedbacks())

@app.route("/webhook", methods=["POST"])
def webhook():
    # Ricevi eventi da altri sistemi (es: Stripe, Zapier, CRM)
    event = request.json
    # Processa evento, logga, rispondi
    return jsonify({"status": "received", "event": event})

# --- ESEMPIO AVVIO ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
