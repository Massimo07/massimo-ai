# ai_mindset_master.py
"""
Mindset Master AI: costruisci mindset di successo, motivazione, focus, resilienza.
Percorsi personalizzati, esercizi, frase del giorno e tracking evoluzione.
"""

import random

class MindsetMasterAI:
    def __init__(self):
        self.phrases = [
            "Credi sempre in te stesso.",
            "Ogni giorno è una nuova opportunità.",
            "La resilienza crea i campioni.",
            "Il successo nasce dalla costanza.",
            "Impara dagli errori: sono il tuo trampolino."
        ]
        self.track = []

    def daily_phrase(self):
        return random.choice(self.phrases)

    def add_progress(self, note):
        self.track.append(note)

    def get_journey(self):
        return self.track
