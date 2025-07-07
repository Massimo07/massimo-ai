"""
Modulo: ai_growth_predictor.py
Growth predictor: prevede crescita personale, team, guadagni, ranking futuro. Simula “what if”, consiglia azioni strategiche.
"""

import random

def predict_growth(current_pv, referral, activity, months=3):
    factor = 1 + (referral * 0.12) + (activity * 0.08)
    future_pv = int(current_pv * (factor ** months))
    advice = "Per accelerare la crescita, aumenta le azioni quotidiane e motiva almeno 2 nuovi membri."
    return {"forecast": future_pv, "advice": advice}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(predict_growth(30000, 5, 1, 6))
