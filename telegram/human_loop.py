"""
Modulo: human_loop.py
Gestione del fallback umano e supervisione: escalation verso operatori reali quando serve (richiesta esplicita, errori, casi complessi, criticità).
Tieni traccia di tutte le richieste umane, logga motivi, integra con dashboard admin (permette supporto e qualità totale).
"""

import logging

logger = logging.getLogger(__name__)

# Lista degli operatori disponibili (demo: sostituisci con gestione reale)
OPERATORS = [
    {"name": "Massimo", "telegram_id": 111111111, "email": "massimo.ai.official@gmail.com"},
    {"name": "Fabio", "telegram_id": 222222222, "email": "fabio@example.com"}
]

def find_available_operator():
    """
    Trova un operatore disponibile (logica demo, da collegare a DB/CRM reale).
    """
    return OPERATORS[0]  # in futuro: logica di turni, carico, preferenze...

async def escalate_to_human(update, context, reason=""):
    """
    Escalation di una richiesta a operatore umano (via Telegram, Email, dashboard).
    """
    user = update.effective_user
    op = find_available_operator()
    logger.info(f"Escalation a operatore: {op['name']} per utente {user.id}, motivo: {reason}")
    # Notifica all’operatore su Telegram (puoi inviare anche via email/dashboard)
    await context.bot.send_message(
        chat_id=op["telegram_id"],
        text=(
            f"⚠️ Escalation richiesta da utente {user.id} (@{user.username}):\n"
            f"Motivo: {reason}\n"
            f"Messaggio: {update.message.text}"
        )
    )
    # Notifica all’utente
    await update.message.reply_text(
        "📞 Sto passando la tua richiesta a un membro reale del team Massimo AI. Ti risponderà a breve!"
    )
    # Puoi loggare la richiesta anche in DB (per audit e qualità)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    import asyncio
    class DummyUpdate:
        effective_user = type("u", (), {"id": 999, "username": "testuser"})()
        message = type("m", (), {"text": "Voglio parlare con operatore", "reply_text": print})()
    class DummyContext:
        class Bot:
            async def send_message(self, chat_id, text):
                print(f"[BOT → {chat_id}]: {text}")
        bot = Bot()
    asyncio.run(escalate_to_human(DummyUpdate(), DummyContext(), "Test fallback"))
