"""
Modulo: idea_generator.py
Brainstorming AI: genera idee per campagne, social, eventi, premi, quiz, training, reward, claim, nuovi business — sempre originali e su misura!
"""

import openai

def generate_idea(prompt=""):
    system = "Tu sei il migliore creativo di network marketing d’Europa. Sii concreto e rivoluzionario!"
    full_prompt = "Genera 5 idee nuove per: " + prompt
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": full_prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(generate_idea("motivare il team nel mese di agosto"))
