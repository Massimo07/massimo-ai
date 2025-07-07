# /plugins_ai/ai_website_generator.py

import openai

class AIWebsiteGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_website(self, topic: str, n_sections=4, language="it"):
        prompt = (
            f"Crea una struttura HTML per un sito su '{topic}', {n_sections} sezioni, in lingua {language}. "
            "Per ogni sezione: titolo, paragrafo breve e una call-to-action. Il sito deve essere moderno e responsive."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# site_plugin = AIWebsiteGenerator(api_key="TUA_OPENAI_KEY")
# html = site_plugin.generate_website("Massimo AI: La tua AI evolutiva")
