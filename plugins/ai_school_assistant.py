# /plugins_ai/ai_school_assistant.py

import openai

class AISchoolAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def help_student(self, subject, topic, level="superiori", language="it"):
        prompt = (
            f"Fai da tutor AI di {subject} per livello {level}, tema: {topic}, lingua {language}. "
            "Genera: spiegazione semplice, esercizio pratico con soluzione, quiz di 3 domande, riassunto breve."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# school_plugin = AISchoolAssistant(api_key="TUA_OPENAI_KEY")
# support = school_plugin.help_student("fisica", "leggi di Newton")
