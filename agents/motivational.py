"""
MotivationalAgent – Agente motivazionale AI, genera e invia frasi, coaching, reminder, feedback positivi.
Auto-update, plug-in, audit, storico.
"""

import logging
from typing import List, Optional

class MotivationalAgent:
    """
    Agente AI motivazionale per crescita personale e team.
    """
    def __init__(self, name: str = "MotivationalAgent"):
        self.name = name
        self.motivational_phrases: List[str] = [
            "Non mollare mai, anche quando sembra impossibile.",
            "Il successo arriva a chi non si arrende.",
            "Ogni giorno è il primo passo verso la grandezza.",
        ]
        self.history: List[str] = []

    def get_daily_phrase(self) -> str:
        from random import choice
        phrase = choice(self.motivational_phrases)
        self.history.append(phrase)
        logging.info(f"[MotivationalAgent] Frase motivazionale inviata: {phrase}")
        return phrase

    def add_phrase(self, phrase: str):
        self.motivational_phrases.append(phrase)
        logging.info(f"[MotivationalAgent] Nuova frase aggiunta: {phrase}")

    def explain(self) -> str:
        return f"{self.name} supporta la crescita motivazionale con frasi, reminder e supporto positivo ogni giorno."
