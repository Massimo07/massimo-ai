"""
Modulo: motivator.py
Genera e invia messaggi motivazionali personalizzati (testo, voce, video) per ogni occasione: compleanno, traguardo, anniversario.
"""

import datetime
import openai
import random

def motivational_message(name, occasion):
    prompt = f"Scrivi un messaggio motivazionale per {name} in occasione di {occasion}, ispirato a network marketing e crescita personale."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Sii ispirazionale, positivo, concreto."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

def send_birthday_message(user_id, name):
    msg = motivational_message(name, "compleanno")
    # Qui puoi integrare invio su Telegram/WhatsApp/voce/video!
    print(f"Auguri a {name}: {msg}")

def auto_celebrate(user_data):
    today = datetime.date.today().isoformat()
    if user_data.get("birthday") == today:
        send_birthday_message(user_data["id"], user_data["name"])
    # Traguardi/anniversari: stesso schema!

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(motivational_message("Luca", "il suo primo ordine!"))
