def dispatch_agent(data):
    """
    Sceglie e gestisce la risposta AI in base al task e allo stato emotivo.
    Puoi collegare qui OpenAI, Gemini, Claude, Llama, o modelli custom!
    """
    task = data.get("task", "")
    mood = data.get("mood", "neutro")

    # Logica demo: risposta variabile secondo mood
    if mood == "negativo":
        return "Capisco che non sia un momento facile. Vuoi parlarne o vuoi un consiglio pratico?"
    elif mood == "positivo":
        return f"Fantastico! Allora, come posso aiutarti a fare ancora meglio con: {task}?"
    elif mood == "ansioso":
        return "Facciamo un passo alla volta. Dimmi cosa ti blocca ora e troviamo insieme la soluzione."
    else:
        return f"Ecco cosa posso suggerirti per: {task}"

    # TODO: Qui puoi integrare la tua AI generativa preferita!

