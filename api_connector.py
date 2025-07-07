"""
Modulo: api_connector.py
Connettore API universale: collega Massimo AI con Stripe, Zoom, Mailchimp, WhatsApp, Facebook, Google Sheets. Plug & play.
"""

import requests

def call_api(service, endpoint, data=None, token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    url = f"https://api.{service}.com/{endpoint}"
    resp = requests.post(url, json=data, headers=headers)
    return resp.json()

# --- ESEMPIO USO ---
# print(call_api("stripe", "v1/charges", data={"amount":1000}, token="YOUR_API_KEY"))
