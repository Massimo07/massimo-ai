"""
Modulo: ai_bio_vision.py
AI bio vision: genera bio, headline, presentazioni sempre aggiornate, per ogni membro, ogni nuova sfida/goal, stile motivazionale.
"""

import openai

def generate_bio(user_name, goal):
    prompt = f"Scrivi una bio breve e motivazionale per {user_name} che vuole raggiungere: {goal}."
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Headline, hook e bio potenti, emozionali."},
                  {"role": "user", "content": prompt}]
    )
    return resp["choices"][0]["message"]["content"].strip()

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(generate_bio("Massimo", "la qualifica Black Diamond e l’indipendenza economica"))
