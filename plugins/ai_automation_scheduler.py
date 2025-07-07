# /plugins_ai/ai_automation_scheduler.py

import openai

class AIAutomationScheduler:
    def __init__(self, api_key):
        openai.api_key = api_key

    def schedule_tasks(self, tasks, period, channels, language="it"):
        prompt = (
            f"Schedula queste automazioni: {tasks}, periodo: {period}, canali: {channels}, lingua {language}. "
            "Suggerisci: sequenza ottimale, reminder, follow-up personalizzati, notifiche ai membri."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# auto_plugin = AIAutomationScheduler(api_key="TUA_OPENAI_KEY")
# pianificazione = auto_plugin.schedule_tasks(["newsletter", "follow-up WhatsApp"], "30 giorni", ["email", "WhatsApp", "Telegram"])
