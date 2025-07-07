# /plugins_ai/ai_course_creator.py

import openai

class AICourseCreator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_course(self, topic: str, level="base", language="it"):
        prompt = (
            f"Crea la struttura di un corso completo su '{topic}' per livello {level}, in lingua {language}. "
            "Includi: titolo corso, 5 moduli con titolo e descrizione, 3 quiz per modulo e suggerisci un badge motivazionale finale."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# creator = AICourseCreator(api_key="TUA_OPENAI_KEY")
# corso = creator.create_course("Leadership ai tempi dell'AI")
