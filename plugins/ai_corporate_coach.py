# /plugins_ai/ai_corporate_coach.py

import openai

class AICorporateCoach:
    def __init__(self, api_key, stile="motivazionale"):
        openai.api_key = api_key
        self.stile = stile

    def coach(self, domanda, language="it"):
        prompt = (
            f"Rispondi come coach {self.stile} (in lingua {language}):\n{domanda}\n"
            "Dai una risposta personalizzata, azionabile, con esempio pratico."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# coach_plugin = AICorporateCoach(api_key="TUA_OPENAI_KEY")
# risposta = coach_plugin.coach("Come posso motivare il mio team in un momento difficile?")
