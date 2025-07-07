from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.encoders import jsonable_encoder
from typing import List
import csv, os, uuid, io
from backend.onboarding_smart import onboarding_smart, OnboardingSmartRequest

router = APIRouter()

CSV_FILE = "iscritti_landing.csv"
FIELDNAMES = ["uuid", "settore", "target", "lingua", "valore", "nome", "email", "risposte"]

# Inizializza il file CSV se non esiste
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()

# --------- FUNZIONI UTILITY ----------
def salva_iscritto(d):
    # Proteggi doppie iscrizioni (email)
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        existing = [row["email"] for row in csv.DictReader(f)]
    if d["email"] in existing:
        return False
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(d)
    return True

def lista_iscritti():
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def invia_email_fake(email, nome, mondo):
    # Simula invio email di benvenuto (puoi collegare SMTP vero qui)
    print(f"[EMAIL] Benvenuto {nome} in {mondo}! Email inviata a: {email}")

# --------- LANDING HTML FORM ----------
@router.get("/landing/form/{settore}", response_class=HTMLResponse, tags=["Landing AI"])
def landing_form(settore: str, target: str = "tutti", lingua: str = "it", valore: str = "crescita"):
    data = OnboardingSmartRequest(settore=settore, target=target, lingua=lingua, valore=valore)
    ob = onboarding_smart(data)
    palette = ob["palette"]
    form_fields = ''.join(
        f'<label>{d}<br><input name="risposta_{i}" required style="width:100%"></label><br><br>'
        for i, d in enumerate(ob['domande_onboarding'], 1)
    )
    html = f"""
    <!DOCTYPE html>
    <html lang="{lingua}">
    <head>
      <meta charset="UTF-8" />
      <title>{ob['mondo']} – Iscriviti</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <style>
        body {{
          background: linear-gradient(135deg, {palette[0]}, {palette[1]}, {palette[2]});
          color: #222; font-family: 'Montserrat', sans-serif; min-height: 100vh; margin:0;
          display:flex;flex-direction:column;justify-content:center;align-items:center;
        }}
        .card {{
          background: rgba(255,255,255,0.93); border-radius:2em; box-shadow:0 6px 32px #0002;
          padding:2em; max-width:400px; text-align:center; margin-top:2em;
        }}
        .icona {{ font-size:2.5em; }}
        h1 {{ margin:0.4em 0; font-size:2em; }}
        .claim {{ color:{palette[2]}; font-size:1.1em; font-weight:600; margin-bottom:1.2em; }}
        form {{ margin-top:2em; }}
        button {{
          background: {palette[2]}; color:#fff; border:none; border-radius:1.2em;
          font-size:1.1em; padding:0.7em 2em; margin-top:1em; cursor:pointer;
          box-shadow:0 2px 6px #0002;
        }}
        label {{ text-align:left; display:block; font-weight:500; margin-top:1em; }}
        input {{ border-radius:0.8em; border:1px solid #bbb; padding:0.6em; font-size:1em; margin-top:0.4em; }}
      </style>
    </head>
    <body>
      <div class="card">
        <div class="icona">{ob['icona']}</div>
        <h1>{ob['mondo']}</h1>
        <div class="claim">{ob['claim']}</div>
        <form method="post" action="/landing/invia-form/{settore}">
          <input type="hidden" name="uuid" value="{uuid.uuid4()}">
          <input type="hidden" name="target" value="{target}">
          <input type="hidden" name="lingua" value="{lingua}">
          <input type="hidden" name="valore" value="{valore}">
          <label>Nome<br><input name="nome" required></label>
          <label>Email<br><input name="email" type="email" required></label>
          {form_fields}
          <button type="submit">ISCRIVITI</button>
        </form>
      </div>
    </body>
    </html>
    """
    return HTMLResponse(html)

# --------- RICEVI ISCRIZIONE E COLLEGA ONBOARDING/MEMORY/NOTIFY ----------
@router.post("/landing/invia-form/{settore}", response_class=HTMLResponse, tags=["Landing AI"])
async def ricevi_form(
    request: Request,
    settore: str,
    uuid: str = Form(...),
    target: str = Form(...),
    lingua: str = Form(...),
    valore: str = Form(...),
    nome: str = Form(...),
    email: str = Form(...),
    risposta_1: str = Form(...),
    risposta_2: str = Form(...),
    risposta_3: str = Form(...),
):
    risposte = [risposta_1, risposta_2, risposta_3]
    iscritto = {
        "uuid": uuid,
        "settore": settore,
        "target": target,
        "lingua": lingua,
        "valore": valore,
        "nome": nome,
        "email": email,
        "risposte": "|".join(risposte)
    }
    if not salva_iscritto(iscritto):
        return HTMLResponse(f"<html><body style='font-family:sans-serif;text-align:center;'><h2>Questa email risulta già iscritta!</h2><a href='/'>Torna alla Home</a></body></html>")
    # Simula invio email di benvenuto
    from backend.onboarding_smart import onboarding_smart, OnboardingSmartRequest
    ob_data = OnboardingSmartRequest(settore=settore, target=target, lingua=lingua, valore=valore)
    ob = onboarding_smart(ob_data)
    invia_email_fake(email, nome, ob["mondo"])
    # (Collega qui memory, dashboard, notifiche, automazioni reali)
    return HTMLResponse(f"""
      <html><body style="font-family:sans-serif; text-align:center; padding:4em;">
      <h2>Grazie {nome}, sei ufficialmente iscritto a <b>{ob['mondo']}</b>!</h2>
      <p>Riceverai info e onboarding personalizzato via email.<br>
      <a href='/'>Torna alla Home</a>
      </p></body></html>
    """)

# --------- ENDPOINT LISTA ISCRITTI (API) ----------
@router.get("/landing/iscritti", response_class=JSONResponse, tags=["Landing AI"])
def get_iscritti():
    return lista_iscritti()

# --------- EXPORT CSV/EXCEL ---------
@router.get("/landing/export/csv", response_class=StreamingResponse, tags=["Landing AI"])
def export_csv():
    f = open(CSV_FILE, "rb")
    return StreamingResponse(f, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=iscritti_landing.csv"})

@router.get("/landing/export/excel", tags=["Landing AI"])
def export_excel():
    try:
        import pandas as pd
        df = pd.read_csv(CSV_FILE)
        output = io.BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return StreamingResponse(output, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                 headers={"Content-Disposition": "attachment; filename=iscritti_landing.xlsx"})
    except ImportError:
        return JSONResponse({"errore": "Installare pandas per export excel: pip install pandas openpyxl"}, status_code=500)
