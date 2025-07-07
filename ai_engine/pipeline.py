"""
pipeline.py – Gestione pipeline multi-step per elaborazioni AI complesse.

Supporta fallback modelli, filtri e trasformazioni.
"""

import logging
from typing import Any, Dict, Optional

from .engine import Engine

class Pipeline:
    """
    Pipeline AI che coordina più engine e step.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.engines = [Engine(name) for name in self.config.get("models", ["default-model"])]
        logging.info(f"[Pipeline] Inizializzata con modelli: {[e.model_name for e in self.engines]}")

    async def process(self, prompt: str, user_context: Optional[Dict[str, Any]] = None) -> Any:
        """
        Elabora il prompt passando sequenzialmente tra modelli e filtri.

        Args:
            prompt (str): Input testo.
            user_context (dict, optional): Contesto utente.

        Returns:
            Any: Risultato finale pipeline.
        """
        current_output = prompt
        for engine in self.engines:
            try:
                current_output = await engine.infer(current_output)
                logging.debug(f"[Pipeline] Output da {engine.model_name}: {current_output}")
            except Exception as e:
                logging.error(f"[Pipeline] Errore su modello {engine.model_name}: {e}", exc_info=True)
                # Fallback o gestione errore
        logging.info("[Pipeline] Processo completato con successo.")
        return current_output
