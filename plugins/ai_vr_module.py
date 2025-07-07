# /plugins_ai/ai_vr_module.py

import openai

class AIVRModule:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_vr_scenario(self, topic: str, language="it"):
        prompt = (
            f"Crea la descrizione dettagliata di uno scenario immersivo VR su '{topic}', in lingua {language}. "
            "Deve includere: ambientazione, personaggi, attività possibili, missione/obiettivo, elementi interattivi."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# vr_plugin = AIVRModule(api_key="TUA_OPENAI_KEY")
# scenario = vr_plugin.generate_vr_scenario("Leadership in una sala conferenze virtuale")
