"""
Modulo: ai_infinite_content.py
Genera micro-learning, quiz, post, audio, storie, video, contenuti sempre nuovi su ogni topic. Auto-aggiorna ogni giorno: il team non si annoia mai!
"""

import openai
import datetime

def generate_content(topic="network marketing"):
    prompt = f"Genera ogni giorno un contenuto originale e motivante su: {topic}. Sii conciso, concreto e utile."
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Contenuti sempre freschi, motivazionali, azionabili."},
                  {"role": "user", "content": prompt}]
    )
    content = resp["choices"][0]["message"]["content"].strip()
    date = datetime.date.today().isoformat()
    return {"date": date, "topic": topic, "content": content}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(generate_content("leadership"))
