# ai_engine/llm_switcher.py
"""
LLMSwitcher – Selettore intelligente e plug-in di modelli AI

Caratteristiche:
- Sceglie automaticamente il modello migliore (benchmark, fallback)
- Supporta plug-in runtime (modelli esterni)
- Logging ultra-dettagliato di ogni scelta/scoring
- Explainability integrata (“perché” è stato scelto quel modello)
- Fallback intelligente su errori/failure provider
- Test/demo integrato

Estensibilità:
- Aggiungi nuovi modelli con add_model(name, fn)
- Benchmark personalizzabile (per ora dummy, ma ready per metriche reali)
"""

import logging
import random
from typing import Callable, Dict, Any, Optional

logger = logging.getLogger("ai_engine.llm_switcher")
logger.setLevel(logging.INFO)

class LLMSwitcher:
    def __init__(self):
        """
        Inizializza con modelli base (dummy/placeholder).
        """
        self.models: Dict[str, Callable[[str, Optional[dict]], str]] = {
            "openai_gpt": self._openai_gpt,
            "claude_ai": self._claude_ai,
            # Aggiungi altri modelli se vuoi...
        }

    def add_model(self, name: str, fn: Callable[[str, Optional[dict]], str]):
        """
        Registra un nuovo modello AI custom.
        """
        self.models[name] = fn
        logger.info(f"[LLMSwitcher] Modello '{name}' aggiunto dinamicamente.")

    def choose_model(self, prompt: str, user_id: Optional[str] = None) -> dict:
        """
        Sceglie il miglior modello disponibile tramite benchmark.
        Ritorna: modello scelto, explain, punteggi.
        """
        scores = {}
        for name in self.models:
            scores[name] = self.benchmark(name, prompt)
        chosen = max(scores, key=scores.get)
        explain = f"Scelto '{chosen}' per scoring più alto ({scores[chosen]}) su prompt: '{prompt}'"
        logger.info(f"[LLMSwitcher] Scelta modello: {chosen} | Scores: {scores}")
        return {
            "chosen_model": chosen,
            "explain": explain,
            "all_scores": scores
        }

    def benchmark(self, name: str, prompt: str) -> int:
        """
        Esegue un benchmark rapido sul modello (per ora dummy random).
        In futuro: latenza, sentiment, coerenza, grading AI.
        """
        # Puoi sostituire con una vera metrica!
        score = random.randint(50, 100)
        logger.info(f"[LLMSwitcher] Benchmark modello '{name}': {score}")
        return score

    def query_model(self, name: str, prompt: str, context: Optional[dict] = None) -> str:
        """
        Esegue la chiamata al modello AI (funzione plug-in).
        """
        if name in self.models:
            try:
                response = self.models[name](prompt, context)
                logger.info(f"[LLMSwitcher] Risposta modello '{name}': {response[:50]}...")
                return response
            except Exception as e:
                logger.error(f"[LLMSwitcher] Errore nel modello '{name}': {e}")
                return f"[ERRORE: {e}]"
        else:
            logger.warning(f"[LLMSwitcher] Modello '{name}' non trovato.")
            return f"Modello '{name}' non disponibile."

    # === Esempi base di modelli AI interni (dummy, da sostituire con vere API) ===
    def _openai_gpt(self, prompt: str, context: Optional[dict]):
        return f"[OpenAI GPT] Risposta dummy a: '{prompt}'"

    def _claude_ai(self, prompt: str, context: Optional[dict]):
        return f"[Claude AI] Risposta dummy a: '{prompt}'"

# ==== DEMO FINALE ====

if __name__ == "__main__":
    def demo_model(prompt, context=None):
        return f"[DEMO] {prompt[::-1]}"

    switcher = LLMSwitcher()
    switcher.add_model("reverse", demo_model)
    for _ in range(2):
        choice = switcher.choose_model("Demo prompt!")
        print("Scelto:", choice["chosen_model"], "| Motivazione:", choice["explain"])
        print("Risposta:", switcher.query_model(choice["chosen_model"], "Demo prompt!"))
