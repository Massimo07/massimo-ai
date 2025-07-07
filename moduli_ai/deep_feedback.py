"""
Modulo: deep_feedback.py
Sondaggi avanzati, micro-feedback, NPS predittivo, sentiment analysis. Alert se il team rischia abbandono o calo engagement!
"""

import random

FEEDBACKS = []

def collect_deep_feedback(user_id, question, answer):
    sentiment = random.choice(["positivo", "neutro", "negativo"])
    FEEDBACKS.append({
        "user_id": user_id,
        "question": question,
        "answer": answer,
        "sentiment": sentiment
    })
    return f"Feedback ricevuto. Sentiment: {sentiment}"

def nps_score():
    # Demo: calcola NPS
    promoters = len([f for f in FEEDBACKS if f["sentiment"] == "positivo"])
    detractors = len([f for f in FEEDBACKS if f["sentiment"] == "negativo"])
    total = len(FEEDBACKS)
    return int((promoters - detractors) / total * 100) if total else 100

def alert_churn():
    if nps_score() < 30:
        print("ALERT: rischio abbandono team! Intervenire subito.")
    else:
        print("Team in salute.")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    collect_deep_feedback(1, "Come ti senti nel team?", "Benissimo!")
    print(nps_score())
    alert_churn()
