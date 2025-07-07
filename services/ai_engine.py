"""
services/ai_engine.py – Orchestratore AI multi-provider (livello servizi)
Gestisce fallback, monitoraggio, modelli custom, iniezione prompt, memory, routing API esterne.
"""
from core.ai_engine import AIEngine
from core.logger import massimo_logger

class AIService:
    def __init__(self, models=None):
        self.engine = AIEngine(models)

    def generate(self, prompt, user_id=None, **kwargs):
        risposta = self.engine.run(prompt, user_id, **kwargs)
        massimo_logger.info("AIService.generate", prompt=prompt, user_id=user_id)
        return risposta

    def chat(self, messages: list, user_id=None, **kwargs):
        # Simula una chat, memory base (implementa sequenze reali GPT etc.)
        full_prompt = "\n".join(m["content"] for m in messages)
        return self.generate(full_prompt, user_id, **kwargs)

ai_service = AIService(["openai", "claude", "llama"])

# Esempio:
# from services.ai_engine import ai_service
# print(ai_service.generate("Crea un business plan in 10 punti."))
