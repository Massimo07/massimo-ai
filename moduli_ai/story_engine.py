"""
Modulo: story_engine.py
Genera storie motivazionali/personalizzate su ogni membro: storytelling emozionale, esempio di successo, condivisione social!
"""

import openai

def generate_story(user_name, role, result):
    prompt = f"Racconta una breve storia emozionale di {user_name}, {role}, che ha raggiunto {result}, ispirando altri a provarci. Sii concreto e reale."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Sii emozionale, motivante, breve, realista."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(generate_story("Giorgia", "studentessa", "il suo primo bonus Live On Plus"))
