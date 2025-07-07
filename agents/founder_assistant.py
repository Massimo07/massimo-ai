"""
FounderAssistant – Agente “virtual CEO”, assistente personale del founder/team.
Prompt AI avanzato, audit, gestione conversazione, memoria breve/long-term.
"""

import logging
from typing import Any, Dict, List, Optional

class FounderAssistant:
    """
    Agente Assistant personale per founder/CEO. Offre supporto strategico e operativo.
    """
    def __init__(self, name: str = "FounderAssistant"):
        self.name = name
        self.conversation: List[Dict[str, Any]] = []

    def process_message(self, message: str, user: str = "founder") -> str:
        response = f"{self.name}: Ciao {user}, ecco la risposta personalizzata alla tua domanda: '{message}'"
        self._log_conversation(user, message, response)
        return response

    def _log_conversation(self, user: str, message: str, response: str):
        entry = {"user": user, "message": message, "response": response}
        self.conversation.append(entry)
        logging.info(f"[FounderAssistant] {user} >> {message} | RISPOSTA: {response}")

    def get_history(self) -> List[Dict[str, Any]]:
        return self.conversation

    def explain(self) -> str:
        return f"{self.name} assiste il founder nel decision making, nel coaching AI e nella produttività personale."
