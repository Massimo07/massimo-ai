"""
Modulo: mentor_ai.py
Mentor motivazionale AI — crea piani giornalieri, esercizi, check, quiz ispirati al libro di Massimo. Personalizzato per ogni membro.
"""

import datetime
import data_manager
import openai_service

MENTOR_PATH = "mentor_journey.json"

def start_mentor(user_id):
    # Primo piano motivazionale (genera con AI su misura!)
    today = datetime.date.today().isoformat()
    plan = {
        "start": today,
        "steps": [
            {"day": 1, "action": "Leggi il capitolo 1 del libro 'Rivoluziona la tua vita...' e scrivi cosa ti colpisce."},
            {"day": 2, "action": "Fai l'esercizio delle 3 priorità per il tuo obiettivo."},
            {"day": 3, "action": "Invia a Massimo AI 1 domanda sul business che ti preoccupa di più."},
            {"day": 4, "action": "Quiz motivazionale AI: rispondi alle domande per scoprire i tuoi punti di forza!"},
            {"day": 5, "action": "Crea il tuo mantra personale e condividilo nel community hub."}
        ],
        "completed": []
    }
    data_manager.update_user_data(user_id, mentor_plan=plan)
    return plan

def check_step(user_id, day, response):
    user = data_manager.get_user_data(user_id)
    plan = user.get("mentor_plan", {})
    if not plan: return "Piano non avviato!"
    for step in plan.get("steps", []):
        if step["day"] == day and step not in plan.get("completed", []):
            plan.setdefault("completed", []).append(step)
            data_manager.update_user_data(user_id, mentor_plan=plan)
            # Feedback AI
            ai_feedback = openai_service.ask_massimo(f"Dai un feedback motivazionale a questo esercizio:\n{response}")
            return f"Step {day} completato! {ai_feedback}"
    return "Step già completato o non trovato."

# --- ESEMPIO USO ---
if __name__ == "__main__":
    plan = start_mentor(1)
    print(plan)
    print(check_step(1, 2, "Ho fatto la lista delle mie priorità."))
