# /plugins_ai/ai_sport_coach.py

import openai

class AISportCoach:
    def __init__(self, api_key):
        openai.api_key = api_key

    def personal_program(self, sport, goals, experience="beginner", language="it"):
        prompt = (
            f"Agisci come coach di {sport} per un atleta {experience}, obiettivi: {goals}, lingua {language}. "
            "Genera: piano allenamento 7 giorni, motivazione, consigli alimentari, esercizi mentali."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# sport_plugin = AISportCoach(api_key="TUA_OPENAI_KEY")
# program = sport_plugin.personal_program("calcio", "aumentare resistenza e velocità", "avanzato")
