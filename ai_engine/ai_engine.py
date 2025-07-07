"""
ai_engine.py – Motore centrale AI per orchestrare modelli e pipeline.

Gestisce configurazioni, fallback, metriche e monitoraggio.
"""

import logging
from typing import Any, Dict, Optional
from .pipeline import Pipeline

class AIEngine:
    """
    Motore AI principale che coordina pipeline e modelli AI.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.pipeline = Pipeline(self.config.get("pipeline_config", {}))
        logging.info("[AIEngine] Inizializzato con config.")

    async def run(self, prompt: str, user_context: Optional[Dict[str, Any]] = None) -> Any:
        """
        Esegue il prompt attraverso la pipeline AI.

        Args:
            prompt (str): Testo di input.
            user_context (dict, optional): Contesto utente per personalizzazione.

        Returns:
            Any: Risultato prodotto dalla pipeline.
        """
        try:
            logging.debug(f"[AIEngine] Esecuzione prompt: {prompt}")
            result = await self.pipeline.process(prompt, user_context)
            logging.info("[AIEngine] Prompt processato con successo.")
            return result
        except Exception as e:
            logging.error(f"[AIEngine] Errore in run: {e}", exc_info=True)
            raise
