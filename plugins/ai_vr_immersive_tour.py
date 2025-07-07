# /plugins_ai/ai_vr_immersive_tour.py

import openai

class AIVRImmersiveTour:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_tour(self, place, theme="cultura", language="it"):
        prompt = (
            f"Crea un tour VR immersivo di '{place}', tema: {theme}, lingua {language}. "
            "Suggerisci 5 tappe interattive, narrazione coinvolgente, elementi visivi e audio, 1 minigioco."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# vr_tour_plugin = AIVRImmersiveTour(api_key="TUA_OPENAI_KEY")
# tour = vr_tour_plugin.create_tour("Firenze rinascimentale", "arte")
