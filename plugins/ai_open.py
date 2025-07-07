"""
Modulo: ai_open.py
API REST aperte (public endpoint): consente a partner, plugin esterni, skill esterne di interfacciarsi a Massimo AI (export, import, live info).
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "online", "version": "MAXIMUM"})

@app.route("/api/score", methods=["GET"])
def score():
    # Demo: restituisce punteggio medio AI
    return jsonify({"score": 9.7})

@app.route("/api/export/users", methods=["GET"])
def export_users():
    # Demo: esporta lista utenti (aggiungi security/limiti reali)
    import data_manager
    return jsonify(data_manager.get_all_users())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
