import os
import json
import pycountry
import openai
import time

openai.api_key = "LA_TUA_OPENAI_API_KEY"  # Cambia con la tua!

# Carica chiavi originali (es: base.json in inglese)
with open("base.json", "r", encoding="utf-8") as f:
    base_keys = json.load(f)

output_dir = "i18n"
os.makedirs(output_dir, exist_ok=True)

# Prendi tutte le lingue ISO 639-1
languages = {lang.alpha_2: lang.name for lang in pycountry.languages if hasattr(lang, 'alpha_2')}

for code, lang_name in languages.items():
    file_path = os.path.join(output_dir, f"{code}.json")
    if os.path.exists(file_path):
        continue  # Salta se già esiste
    tradotto = {}
    for key, testo in base_keys.items():
        prompt = f"Translate in '{lang_name}' the following user interface string (do NOT translate the key):\n{testo}\n(Only the translation, no quotes or extra words)"
        try:
            res = openai.ChatCompletion.create(
                model="gpt-4o",  # puoi usare anche "gpt-3.5-turbo" se vuoi risparmiare
                messages=[{"role": "system", "content": prompt}]
            )
            tradotto[key] = res.choices[0].message.content.strip()
            time.sleep(0.5)  # Per evitare rate limit
        except Exception as e:
            tradotto[key] = testo  # fallback inglese
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tradotto, f, indent=4, ensure_ascii=False)
    print(f"Creato: {file_path} – {lang_name}")

print("\n✅ GENERATE ALL LANGUAGE FILES – WORLD READY!")

