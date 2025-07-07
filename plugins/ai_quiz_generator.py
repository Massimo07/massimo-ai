# /plugins_ai/ai_quiz_generator.py

import openai

class AIQuizGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_quiz(self, topic: str, n_questions=5, language="it"):
        prompt = (
            f"Genera un quiz di {n_questions} domande a risposta multipla su '{topic}', in lingua {language}. "
            "Ogni domanda deve avere 4 risposte e spiegazione della risposta corretta."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# quiz_plugin = AIQuizGenerator(api_key="TUA_OPENAI_KEY")
# quiz = quiz_plugin.generate_quiz("Mentalità vincente")
