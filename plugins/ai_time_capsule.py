"""
Modulo: ai_time_capsule.py
Time capsule AI: ogni membro lascia sogno/obiettivo, la AI lo invia tra X mesi con commento personalizzato, analisi progressi, booster motivazionale.
"""

import datetime

TIME_CAPSULE = {}

def save_capsule(user_id, dream, months=6):
    unlock_date = (datetime.date.today() + datetime.timedelta(days=30*months)).isoformat()
    TIME_CAPSULE[user_id] = {"dream": dream, "unlock": unlock_date}
    return f"Messaggio salvato! Lo riceverai il {unlock_date}."

def open_capsule(user_id, progress=None):
    capsule = TIME_CAPSULE.get(user_id)
    if not capsule:
        return "Nessuna capsule trovata!"
    advice = "Complimenti! Hai mantenuto la promessa." if progress == "raggiunto" else "Non mollare: ogni giorno è buono per ripartire."
    return f"Il tuo sogno: '{capsule['dream']}' — Unlock: {capsule['unlock']}\n{advice}"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(save_capsule(1, "Raggiungere 30.000 PV e Black Diamond!", 12))
    print(open_capsule(1, "raggiunto"))
