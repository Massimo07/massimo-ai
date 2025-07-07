# /plugins_ai/ai_microlearning_builder.py

import openai

class AIMicroLearningBuilder:
    def __init__(self, api_key):
        openai.api_key = api_key

    def build_microcourse(self, topic, n_lessons=5, language="it"):
        prompt = (
            f"Crea un micro-corso su '{topic}', {n_lessons} lezioni brevi, ogni lezione massimo 500 caratteri, "
            f"in lingua {language}, con esercizio pratico e tip motivazionale alla fine di ogni lezione."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# micro_plugin = AIMicroLearningBuilder(api_key="TUA_OPENAI_KEY")
# microcourse = micro_plugin.build_microcourse("Time Management")
