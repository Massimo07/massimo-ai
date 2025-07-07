"""
Modulo: ml_monitor.py
Monitoraggio costante qualità AI: valuta risposte, effettua ranking, cambia modello se necessario, report performance e alert.
"""

import feedback
import openai_service
import logging

logger = logging.getLogger("massimoai.ml_monitor")

THRESHOLD_LOW_SCORE = 6

def evaluate_ai_performance(window=100):
    feedbacks = feedback.get_feedbacks()[-window:]
    avg_score = sum(f["score"] for f in feedbacks) / len(feedbacks) if feedbacks else 10
    logger.info(f"AI score medio: {avg_score}")
    return avg_score

def maybe_switch_model():
    avg_score = evaluate_ai_performance()
    if avg_score < THRESHOLD_LOW_SCORE:
        openai_service.set_model("gpt-4o")  # Switch a modello più potente!
        logger.warning("AI model switch: performance bassa, cambio modello!")
        return "Model switched!"
    return "All good!"

if __name__ == "__main__":
    print(evaluate_ai_performance())
    print(maybe_switch_model())
