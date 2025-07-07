# /plugins_ai/ai_naming_generator.py

import openai

class AINamingGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_names(self, context, n_names=5, style="innovativo", language="it"):
        prompt = (
            f"Genera {n_names} nomi {style} per {context}, in lingua {language}. "
            "Per ogni nome, spiega il significato e suggerisci un payoff o slogan."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# naming_plugin = AINamingGenerator(api_key="TUA_OPENAI_KEY")
# nomi = naming_plugin.generate_names("nuova app AI per studenti", 7, "ispirazionale")
