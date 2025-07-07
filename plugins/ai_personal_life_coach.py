# /plugins_ai/ai_personal_life_coach.py

import openai

class AIPersonalLifeCoach:
    def __init__(self, api_key):
        openai.api_key = api_key

    def coach_me(self, challenge, goal, language="it"):
        prompt = (
            f"Fai da coach personale AI. Sfida: {challenge}, obiettivo: {goal}, lingua {language}. "
            "Suggerisci: piano d’azione, esercizi, riflessioni motivazionali, frasi ispirazionali, come superare blocchi."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# coach_plugin = AIPersonalLifeCoach(api_key="TUA_OPENAI_KEY")
# coaching = coach_plugin.coach_me("mancanza di motivazione", "imparare una nuova competenza")
