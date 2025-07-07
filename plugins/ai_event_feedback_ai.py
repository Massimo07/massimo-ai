"""
Modulo: ai_event_feedback_ai.py
Feedback AI: raccoglie feedback evento, crea wordcloud/analisi, video insight, suggerimenti personalizzati per migliorare ogni evento futuro.
"""

FEEDBACKS = []

def collect_feedback(event, user_id, feedback):
    FEEDBACKS.append({"event": event, "user_id": user_id, "feedback": feedback})
    return f"Feedback ricevuto da {user_id} su '{event}'."

def feedback_insight(event):
    texts = [f["feedback"] for f in FEEDBACKS if f["event"] == event]
    if not texts:
        return "Nessun feedback ancora."
    # Demo: crea wordcloud, insight AI
    keywords = set(word for text in texts for word in text.split() if len(word) > 4)
    insight = f"Wordcloud: {', '.join(keywords)}"
    return insight

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(collect_feedback("Magic Team World Summit", 1, "Evento carico di energia e valore, networking unico!"))
    print(feedback_insight("Magic Team World Summit"))
