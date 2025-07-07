# /plugins_ai/ai_medical_helper.py

import openai

class AIMedicalHelper:
    def __init__(self, api_key):
        openai.api_key = api_key

    def medical_info(self, symptoms, age="", sex="", language="it"):
        prompt = (
            f"Rispondi come assistente medico informativo. Sintomi: {symptoms}, età: {age}, sesso: {sex}, lingua {language}. "
            "Dai consigli generali di prevenzione, segnala quando consultare un medico vero, non fare mai diagnosi."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# med_plugin = AIMedicalHelper(api_key="TUA_OPENAI_KEY")
# info = med_plugin.medical_info("mal di testa, nausea", "35", "M")
