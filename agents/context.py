"""
Context – Gestione avanzata del contesto operativo per agenti Massimo AI.
Permette la trasmissione sicura di dati di stato, ambiente, meta tra agenti e orchestratori.
"""

from typing import Any, Dict, Optional

class Context:
    """
    Rappresenta il contesto di esecuzione di un agente o workflow.
    """
    def __init__(self, user_id: Optional[str] = None, session_id: Optional[str] = None, meta: Optional[Dict[str, Any]] = None):
        self.user_id = user_id
        self.session_id = session_id
        self.meta = meta or {}

    def set(self, key: str, value: Any):
        """Imposta un valore nel contesto."""
        self.meta[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Recupera un valore dal contesto."""
        return self.meta.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        """Serializza tutto il contesto come dizionario."""
        data = {
            "user_id": self.user_id,
            "session_id": self.session_id,
            "meta": self.meta,
        }
        return data
