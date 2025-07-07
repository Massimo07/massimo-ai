"""
Modulo: bot_scheduler.py
Schedulatore task automatici: drip-campaign, reminder, follow-up, quiz, alert, challenge. Pronto per APScheduler/cron.
"""

from apscheduler.schedulers.background import BackgroundScheduler
import time

scheduler = BackgroundScheduler()

def drip_message(user_id, text, when):
    print(f"Invierò a {user_id}: {text} alle {when}")

def follow_up(user_id, tipo="quiz", after=60):
    print(f"Follow-up per {user_id} dopo {after} secondi ({tipo})")

def schedule_all():
    scheduler.add_job(lambda: drip_message(1, "Hai completato la sfida? Rispondi subito!", "domani"), 'interval', seconds=30)
    scheduler.add_job(lambda: follow_up(1, "quiz", 60), 'interval', seconds=60)
    scheduler.start()

# --- ESEMPIO USO ---
if __name__ == "__main__":
    schedule_all()
    print("Schedulatore attivo! Ctrl+C per fermare.")
    time.sleep(120)
