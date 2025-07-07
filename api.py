
from flask import Flask, request, jsonify
from flask_cors import CORS

print("DEBUG: Massimo AI server è stato avviato!")
# Importa la funzione AI dal file openai_service.py
from openai_service import get_openai_response

app = Flask(__name__)
CORS(app)  # Permette richieste da qualsiasi frontend web/app

# ROUTE PRINCIPALE – Risposta AI reale!
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    question = data.get("question", "")
    answer = get_openai_response(question)
    return jsonify({"answer": answer})

# ROUTE per avviare scraping (quando pronto)
@app.route("/rebuild", methods=["POST"])
def rebuild():
    # result = run_scraping(force=True)   # (decommenta quando hai scraping pronto)
    result = True
    msg = "Scraping avviato con successo." if result else "Errore nell'avvio scraping."
    return jsonify({"status": msg})

# ROUTE status di sistema
@app.route("/status", methods=["GET"])
def status():
    status_info = {
        "status": "OK",
        "products_count": 999, # Da leggere dal DB vero se vuoi
        "last_scrape": "2025-06-20T10:00:00",
        "ai_online": True
    }
    return jsonify(status_info)

# ROUTE esportazione dati
@app.route("/export", methods=["GET"])
def export():
    # export_products_to_csv("products_export.csv") # (decommenta per export reale)
    return jsonify({"url": "/download/products_export.csv"})

if __name__ == "__main__":
    app.run(port=8080, debug=True)

