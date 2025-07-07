import os
import sqlite3
import json
from flask import Flask, render_template_string, request, send_file

DB_PATH = "massimoai_products.db"
CSV_PATH = "massimoai_products.csv"
JSON_PATH = "massimoai_products.json"
PDF_DIR = "schede_prodotti"

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>MASSIMO AI DASHBOARD</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f5f5f7; color: #232323; margin: 0; padding: 0; }
        header { background: #0f2138; color: #fff; padding: 20px 40px; font-size: 2em; font-weight: bold; letter-spacing: 1px; }
        .container { max-width: 1200px; margin: 40px auto; padding: 30px 40px; background: #fff; border-radius: 16px; box-shadow: 0 6px 32px #0002;}
        form { margin-bottom: 28px; }
        input[type=text] { padding: 12px; font-size: 1.2em; border: 1px solid #ccc; border-radius: 6px; width: 40%; margin-right: 16px;}
        button { padding: 12px 24px; font-size: 1em; background: #235a97; color: #fff; border: none; border-radius: 8px; cursor: pointer;}
        button.export { background: #55a35a; margin-left: 8px;}
        table { width: 100%; border-collapse: collapse; margin-top: 22px; }
        th, td { border-bottom: 1px solid #e0e0e0; padding: 12px 8px; text-align: left; }
        th { background: #f0f3fa; }
        img { max-width: 80px; border-radius: 10px;}
        .pdf-link { color: #bf3b19; font-weight: bold;}
        .actions { margin-top: 24px;}
        .actions a { margin-right: 14px;}
    </style>
</head>
<body>
<header>MASSIMO AI – DASHBOARD 💎</header>
<div class="container">
    <form method="get" action="/">
        <input type="text" name="q" value="{{q}}" placeholder="Cerca prodotto, categoria o parola...">
        <button type="submit">Cerca</button>
        <button class="export" name="export" value="csv">Export CSV</button>
        <button class="export" name="export" value="json">Export JSON</button>
    </form>
    <table>
        <tr>
            <th>Prodotto</th>
            <th>Prezzo</th>
            <th>Categoria</th>
            <th>Immagine</th>
            <th>Scheda PDF</th>
            <th>Link</th>
        </tr>
        {% for row in rows %}
        <tr>
            <td><b>{{row['name']}}</b><br>
                <small>{{row['description'][:60] ~ ("..." if row['description']|length > 60 else "")}}</small>
            </td>
            <td>{{row['price']}}</td>
            <td>{{row['category']}}</td>
            <td>
                {% if row['image_url'] %}
                  <img src="{{row['image_url']}}" alt="Immagine">
                {% endif %}
            </td>
            <td>
                {% if row['pdf_links'] %}
                    {% for pdf in row['pdf_links'].split("|") if pdf %}
                        <a class="pdf-link" href="/pdf/{{pdf.split('/')[-1]}}" target="_blank">PDF</a><br>
                    {% endfor %}
                {% endif %}
            </td>
            <td>
                <a href="{{row['url']}}" target="_blank">Vedi</a>
            </td>
        </tr>
        {% endfor %}
    </table>
    <div class="actions">
        <a href="/?export=csv">Scarica CSV</a>
        <a href="/?export=json">Scarica JSON</a>
    </div>
    <div style="margin-top:28px; color:#888; font-size:0.93em;">
        Totale prodotti: <b>{{rows|length}}</b> &nbsp;– Powered by MASSIMO AI 💎
    </div>
</div>
</body>
</html>
'''

def fetch_rows(q=None):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if q:
        q_like = f"%{q}%"
        cur.execute("""
            SELECT * FROM products WHERE name LIKE ? OR description LIKE ? OR category LIKE ? 
            ORDER BY name ASC LIMIT 100
        """, (q_like, q_like, q_like))
    else:
        cur.execute("SELECT * FROM products ORDER BY name ASC LIMIT 100")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

@app.route("/", methods=["GET"])
def index():
    q = request.args.get("q", "")
    export = request.args.get("export", None)
    rows = fetch_rows(q)
    if export == "csv":
        # Esporta in CSV
        csv_file = "export_massimoai.csv"
        keys = rows[0].keys() if rows else []
        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            import csv
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        return send_file(csv_file, as_attachment=True)
    if export == "json":
        json_file = "export_massimoai.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
        return send_file(json_file, as_attachment=True)
    return render_template_string(TEMPLATE, rows=rows, q=q)

@app.route("/pdf/<filename>")
def serve_pdf(filename):
    # Serve i PDF allegati alla scheda tecnica (devi avere i file PDF in /schede_prodotti/)
    file_path = os.path.join(PDF_DIR, filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    return "File non trovato", 404

if __name__ == "__main__":
    app.run(port=8222, debug=True)

