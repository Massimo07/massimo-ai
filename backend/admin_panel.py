from flask import Flask, render_template_string, request, redirect, url_for, session
import os, json

app = Flask(__name__)
app.secret_key = "CAMBIAQUESTASECRET"

ADMIN_USER = "massimo"
ADMIN_PASS = "adminmax"

DASHBOARD_TEMPLATE = '''
<!DOCTYPE html>
<html><head>
<title>Dashboard Admin Massimo AI</title>
<style>body{font-family:sans-serif;background:#f8f8ff;color:#333} h1{color:#0078D7;} table{width:100%;border-collapse:collapse;} th,td{padding:6px;border:1px solid #ccc} .top{margin-bottom:12px} .logout{float:right} </style>
</head><body>
<div class="top"><h1>Massimo AI - Admin Dashboard</h1>
<a href="{{ url_for('logout') }}" class="logout">Logout</a></div>
<p><b>Totale utenti:</b> {{ stats['utenti'] }} &nbsp;|&nbsp;
<b>Prodotti:</b> {{ stats['prodotti'] }} &nbsp;|&nbsp;
<b>Registrazioni oggi:</b> {{ stats['oggi'] }} </p>
<h2>Prodotti aggiornati</h2>
<table><tr><th>Nome</th><th>Prezzo</th><th>Link</th><th>Descrizione</th></tr>
{% for p in prodotti[:20] %}
<tr><td>{{p['nome']}}</td><td>{{p['prezzo']}}</td><td><a href="{{p['link']}}">link</a></td><td>{{p['descrizione'][:80]}}...</td></tr>
{% endfor %}
</table>
<p><a href="{{url_for('export_prodotti')}}">Scarica tutti i prodotti (.json)</a></p>
<h2>Log Attività</h2>
<pre>{{ logs }}</pre>
</body></html>
'''

@app.route('/admin', methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if request.form.get("user") == ADMIN_USER and request.form.get("pass") == ADMIN_PASS:
            session["admin"] = True
            return redirect(url_for("dashboard"))
    return '''
    <h2>Login Admin Massimo AI</h2>
    <form method="post">
    <input name="user" placeholder="user"><br>
    <input name="pass" type="password" placeholder="password"><br>
    <button type="submit">Login</button>
    </form>
    '''

@app.route('/dashboard')
def dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    # Statistiche demo
    prodotti = []
    stats = {"utenti": 99, "prodotti": 0, "oggi": 0}
    logs = "Startup - Scraping avviato
"
    try:
        data_file = os.path.join(os.path.dirname(__file__), "../data/prodotti_liveonplus.json")
        with open(data_file, encoding="utf-8") as f:
            prodotti = json.load(f)
        stats["prodotti"] = len(prodotti)
    except: pass
    return render_template_string(DASHBOARD_TEMPLATE, prodotti=prodotti, stats=stats, logs=logs)

@app.route('/export_prodotti')
def export_prodotti():
    data_file = os.path.join(os.path.dirname(__file__), "../data/prodotti_liveonplus.json")
    return open(data_file, "rb").read(), 200, {'Content-Type': 'application/json'}

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("admin_login"))

def start_admin_dashboard():
    from threading import Thread
    t = Thread(target=lambda: app.run(host="0.0.0.0", port=8000, debug=False))
    t.daemon = True
    t.start()
