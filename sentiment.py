"""
Modulo: sentiment.py
Analisi automatica del sentiment: classifica, monitora e segnala risposte, chat e feedback.
Pronto per analytics, scoring, prevenzione abbandoni, chatbot empatico.
"""

import logging
from transformers import pipeline

logger = logging.getLogger(__name__)
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analizza il sentiment di un testo (positivo, negativo, neutro).
    """
    result = sentiment_model(text)
    label = result[0]["label"]
    score = result[0]["score"]
    return {"sentiment": label, "score": score}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(analyze_sentiment("Mi sento motivato grazie a Massimo AI!"))
    print(analyze_sentiment("Non sono soddisfatto."))
