# /autorigenerazione_ai/suggestion_engine.py

import random

class SuggestionEngine:
    def genera_suggerimento(self, context):
        plugin = context.get("plugin", "Generico")
        feature = context.get("funzione_nuova", None)
        idee_base = [
            f"Aggiungi una funzione di auto-analisi dati in {plugin}.",
            f"Implementa notifiche push personalizzate in {plugin}.",
            f"Migliora la sicurezza con autenticazione a 2 fattori in {plugin}.",
            f"Integra un sistema di feedback AI in {plugin}.",
            f"Abilita la personalizzazione del layout in {plugin}.",
            f"Genera report automatici su {plugin}."
        ]
        if feature:
            idee_base.append(f"Implementa la funzione '{feature}' in {plugin}.")
        suggerimento = random.choice(idee_base)
        return {
            "plugin": plugin,
            "suggerimento": suggerimento
        }
