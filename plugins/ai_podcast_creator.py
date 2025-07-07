# /plugins_ai/ai_podcast_creator.py

import openai

class AIPodcastCreator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_podcast(self, topic, guest="", language="it"):
        prompt = (
            f"Crea la scaletta e lo script di un podcast su '{topic}'"
            f"{', con ospite ' + guest if guest else ''}, in lingua {language}. "
            "Genera: titolo, sinossi, domande per l’ospite, script intro, 5 domande top, conclusione ispirazionale."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# podcast_plugin = AIPodcastCreator(api_key="TUA_OPENAI_KEY")
# podcast_plan = podcast_plugin.create_podcast("Intelligenza artificiale nella vita quotidiana", "Massimo Marfisi")
