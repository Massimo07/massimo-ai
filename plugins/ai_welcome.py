"""
Modulo: ai_welcome.py
Onboarding AI: genera messaggio testo/audio/video motivazionale, quiz, raccolta dati, prime azioni. Pronto per Telegram/WhatsApp/web!
"""

import openai

def ai_welcome_message(user_name):
    prompt = f"Scrivi un messaggio di benvenuto motivazionale e unico per {user_name}, nuovo iscritto Magic Team, ispirato alla crescita personale e a Massimo AI."
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Sii coinvolgente, sincero, ispirazionale."},
                  {"role": "user", "content": prompt}]
    )
    return resp["choices"][0]["message"]["content"].strip()

def ai_welcome_quiz():
    # Domande base onboarding
    return [
        {"q": "Perché vuoi far parte di Magic Team?", "type": "open"},
        {"q": "Hai già fatto network marketing?", "type": "choice", "a": ["Sì", "No"]},
        {"q": "Qual è il tuo obiettivo nei prossimi 3 mesi?", "type": "open"}
    ]

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(ai_welcome_message("Sara"))
    print(ai_welcome_quiz())
