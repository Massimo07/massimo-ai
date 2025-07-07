# /plugins_ai/ai_language_trainer.py

import openai

class AILanguageTrainer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def language_course(self, lang_from="it", lang_to="en", topic="business", level="base"):
        prompt = (
            f"Crea un mini-corso di lingua da {lang_from} a {lang_to}, tema: {topic}, livello {level}. "
            "Includi: 5 micro-lezioni, dialoghi pratici, esercizi, 10 vocaboli chiave con pronuncia."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# lang_plugin = AILanguageTrainer(api_key="TUA_OPENAI_KEY")
# corso = lang_plugin.language_course("it", "es", "viaggi", "intermedio")
