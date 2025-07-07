"""
Modulo: ai_emotion_translator.py
Emotion Translator: trasforma emozioni in azioni, grafiche, audio, training; ogni emozione è energia utile e connessione per tutto il Magic Team!
"""

def translate_emotion(user_id, emotion):
    if emotion == "gioia":
        return f"{user_id} trasforma la gioia in un post di ringraziamento e una playlist condivisa."
    elif emotion == "paura":
        return f"{user_id} trasforma la paura in una challenge: affronta oggi una piccola cosa che lo spaventa."
    elif emotion == "rabbia":
        return f"{user_id} usa la rabbia per fare sport o creare una grafica potente per il team."
    else:
        return f"{user_id} trasforma {emotion} in un’azione creativa e condivisione."

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(translate_emotion("Massimo", "gioia"))
    print(translate_emotion("Massimo", "paura"))
