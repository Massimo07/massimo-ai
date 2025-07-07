# /plugins_ai/ai_presentation_creator.py

import openai

class AIPresentationCreator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_presentation(self, topic: str, n_slides=8, language="it"):
        prompt = (
            f"Crea una presentazione PowerPoint su '{topic}', {n_slides} slide, "
            "ogni slide con titolo e 3 punti chiave, in lingua {language}."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# pres_plugin = AIPresentationCreator(api_key="TUA_OPENAI_KEY")
# pres = pres_plugin.create_presentation("AI e futuro del business")
