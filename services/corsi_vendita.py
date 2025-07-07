from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Struttura corsi in 3 parti
CORSI_VENDITA = {
    "parte1": [
        ("Ascolta davvero il cliente", "Lezione pratica sull'ascolto attivo con esempio reale."),
        ("Presenta il prodotto con semplicità", "Come presentare senza 'spingere', con esempio."),
        ("Parla con il corpo, non solo parole", "Il linguaggio non verbale nella vendita."),
        ("Quiz: le 3 regole d’oro", "Quiz finale parte 1.")
    ],
    "parte2": [
        ("Gestisci le obiezioni", "Esempi e risposte alle obiezioni più comuni."),
        ("Costruisci relazioni vere", "Diventa un consulente, non un venditore."),
        ("Cura del cliente dopo la vendita", "Come seguire e coccolare il cliente."),
        ("Quiz: cosa NON dire mai", "Quiz finale parte 2.")
    ],
    "parte3": [
        ("Vendere coi social", "Racconta la tua esperienza vera."),
        ("Gestione del tempo", "Organizza la giornata, senza stress."),
        ("Etica nella vendita", "Mai bugie, mai pressione."),
        ("Quiz: metti in pratica", "Quiz finale parte 3.")
    ]
}

def make_corso_keyboard(parte):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{i+1}. {titolo}", callback_data=f"corso_vendita_step_{parte}_{i}")]
        for i, (titolo, testo) in enumerate(CORSI_VENDITA[parte])
    ] + [[InlineKeyboardButton("⬅️ Indietro", callback_data="corsi_vendita_menu")]])

async def corsi_vendita_menu_handler(update, context):
    query = update.callback_query
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Corso Vendita – Parte 1", callback_data="corso_vendita_step_parte1_0")],
        [InlineKeyboardButton("Corso Vendita – Parte 2", callback_data="corso_vendita_step_parte2_0")],
        [InlineKeyboardButton("Corso Vendita – Parte 3", callback_data="corso_vendita_step_parte3_0")],
        [InlineKeyboardButton("⬅️ Indietro", callback_data="home")]
    ])
    await query.edit_message_text("👨‍💼 Scegli la parte del corso vendita:", reply_markup=keyboard)

async def corso_vendita_step_handler(update, context):
    query = update.callback_query
    parts = query.data.split("_")
    parte = parts[3]
    idx = int(parts[4])
    titolo, testo = CORSI_VENDITA[parte][idx]
    # Tastiera avanti/indietro
    buttons = []
    if idx > 0:
        buttons.append(InlineKeyboardButton("⬅️ Indietro", callback_data=f"corso_vendita_step_{parte}_{idx-1}"))
    if idx < len(CORSI_VENDITA[parte]) - 1:
        buttons.append(InlineKeyboardButton("➡️ Avanti", callback_data=f"corso_vendita_step_{parte}_{idx+1}"))
    buttons.append(InlineKeyboardButton("🏠 Home", callback_data="home"))
    keyboard = InlineKeyboardMarkup([buttons])
    await query.edit_message_text(f"*{titolo}*\n\n{testo}", parse_mode="Markdown", reply_markup=keyboard)
