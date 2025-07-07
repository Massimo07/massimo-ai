
def risposte_start(testo):
    if "ordine" in testo:
        return "Puoi fare l'ordine direttamente dal sito Live On Plus nella tua area personale."
    elif "registrazione" in testo:
        return "Per registrarti vai sul link di iscrizione fornito dal tuo sponsor."
    elif "piano" in testo:
        return "Il piano marketing Live On Plus prevede guadagni immediati, ricorrenti e bonus carriera."
    elif "prodotti" in testo:
        return "Abbiamo prodotti per benessere, casa, bellezza e molto altro!"
    else:
        return "Rispondo solo su argomenti relativi a Live On Plus. Chiedimi pure!"
