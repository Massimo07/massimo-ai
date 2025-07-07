"""
Modulo: ai_fear_buster.py
Individua e sblocca paure/blocchi mentali del team: risposte personalizzate, tecniche AI di coaching, audio motivazionali, micro-esercizi pratici.
"""

import random

FEARS = ["paura di parlare in pubblico", "paura del rifiuto", "timidezza", "blocco decisionale"]

def detect_fear(message):
    for f in FEARS:
        if f in message.lower():
            return f
    return None

def bust_fear(fear):
    tips = {
        "paura di parlare in pubblico": "Respira, preparati su un argomento che ami e prova davanti a uno specchio.",
        "paura del rifiuto": "Ogni no è un passo verso il sì. Trasforma il rifiuto in lezione di crescita!",
        "timidezza": "Fai un piccolo gesto fuori dalla tua zona comfort ogni giorno.",
        "blocco decisionale": "Decidi in base ai tuoi valori, non alla paura di sbagliare. L’azione batte l’indecisione!"
    }
    return tips.get(fear, "Coraggio! Ogni paura può essere superata con piccoli passi e il supporto del team.")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    msg = "Oggi sento una forte paura di parlare in pubblico."
    fear = detect_fear(msg)
    print(bust_fear(fear))
