"""
Modulo: copy_ai.py
AI copywriter: crea post, headline, email, script video, bio, inviti, promozioni, tutto ottimizzato e multilingua.
"""

import openai

def generate_copy(prompt, lang="it"):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": f"Scrivi un testo marketing in {lang}:"},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(generate_copy("Promuovi l'opportunità Live On Plus per chi vuole cambiare vita!", lang="it"))
