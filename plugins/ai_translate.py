"""
Modulo: ai_translate.py
Traduzione AI multilingua: ogni messaggio, post, quiz, supporto tradotto istantaneamente, con tono e stile. Pronto per multilingua reale!
"""

import openai

def ai_translate(text, target_lang="en"):
    prompt = f"Traduci in {target_lang} con tono motivazionale e professionale:\n{text}"
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp["choices"][0]["message"]["content"].strip()

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(ai_translate("Unisciti ora al Magic Team e trasforma la tua vita!", "fr"))
