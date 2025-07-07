"""
Modulo: web_push.py
Invia notifiche push su web/app/mobile. Ogni evento, drip, reward, promemoria, alert. Pronto per Firebase/Web Push API.
"""

def send_web_push(user_id, title, body, url="https://magicteam.live"):
    # In reale: integri Firebase, OneSignal o Web Push API (qui solo demo)
    print(f"Notifica PUSH a {user_id}: {title} — {body} — {url}")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    send_web_push(1, "Nuova Challenge!", "Partecipa alla Sfida Diamond ora!", "https://magicteam.live/challenge")
