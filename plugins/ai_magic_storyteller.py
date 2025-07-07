"""
Modulo: ai_magic_storyteller.py
Crea narrazioni di team, trasforma dati reali in storie motivazionali, script video, podcast, presentazioni, contenuti multimediali.
"""

import openai

def team_story(data):
    prompt = f"Crea una narrazione motivazionale che racconta come il team Magic Team ha raggiunto {data['goal']} grazie a {data['action']}, mostrando i risultati di {data['results']}."
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Narrazione emozionale, avvincente, ispirazionale."},
                  {"role": "user", "content": prompt}]
    )
    return resp["choices"][0]["message"]["content"].strip()

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(team_story({
        "goal": "30.000 PV in 1 mese",
        "action": "challenge settimanali e onboarding smart",
        "results": "Sara, Luca, Giorgio hanno superato i loro record personali"
    }))
