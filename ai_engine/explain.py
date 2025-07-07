# ai_engine/explain.py
"""
EXPLAIN – Explainability engine (Massimo AI)

- Traccia motivazione scelte AI
- Audit log spiegazione
- Output leggibile per utente/founder
"""

from ai_engine.logging import ai_logger

def explain_decision(model_name, input_data, result, reason):
    explain = f"Modello '{model_name}' scelto – Reason: {reason} | Input: {input_data} | Output: {result}"
    ai_logger.info(f"[explain] {explain}")
    return explain
