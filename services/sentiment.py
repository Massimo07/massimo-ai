# Analisi del sentimento: puoi collegare GPT, modelli ML, API specifiche...
# Per ora semplice demo con regole base.

def analyze_sentiment(text, lang="it"):
    """
    Analizza il sentimento del testo (demo).
    Puoi collegare modelli avanzati!
    """
    lower = text.lower()
    if any(word in lower for word in ["triste", "male", "deluso", "ansia", "stanco", "solitudine"]):
        return "negativo"
    if any(word in lower for word in ["felice", "bene", "entusiasta", "forte", "pronto"]):
        return "positivo"
    if any(word in lower for word in ["ansia", "agitato", "nervoso"]):
        return "ansioso"
    return "neutro"
