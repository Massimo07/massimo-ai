# /models – Massimo AI

Questa cartella contiene **tutti i modelli dati** fondamentali del sistema Massimo AI.  
Ogni modello è progettato per **scalabilità, sicurezza, compatibilità cloud** e può essere usato sia con **Pydantic** (per FastAPI), sia con **ORM** (SQLAlchemy), sia come schema per serializzazione API.

---

## Struttura e Filosofia

- **Ogni modello** rappresenta una “entità reale” della piattaforma (utente, agente AI, abbonamento, pagamento, ecosistema generato, feedback, evento, token…).
- **Standard di qualità enterprise**: tipizzazione completa, descrizione campi, multi-tenant, meta-campi per estensioni, pronto per export, audit, logging e compliance GDPR/AI Act.
- **Estendibile**: puoi sempre aggiungere attributi specifici per esigenze future o verticali, senza rompere la compatibilità.

---

## Elenco modelli inclusi

- `user.py` — Utenti umani e digitali (agenti AI), ruoli, badge, lingua, meta.
- `subscription.py` — Abbonamenti, piani, ricorrenza, scadenze.
- `world.py` — Mondi AI generati (ecosistemi digitali verticali).
- `transaction.py` — Pagamenti, revenue, audit finanziario.
- `feedback.py` — Feedback utenti, survey, rating, NPS.
- `agent.py` — Agenti AI: identità, owner, skill-set, stato.
- `event.py` — Eventi di sistema, onboarding, log, accessi.
- `token.py` — Token di accesso/refresh/API, sicurezza.

---

## Esempio di utilizzo (FastAPI/Pydantic)

```python
from models.user import User

user = User(
    id="123e4567-e89b-12d3-a456-426614174000",
    email="utente@dominio.com",
    name="Mario Rossi",
    password_hash="$argon2id$v=19$...",
    created_at="2025-07-05T12:00:00Z"
)
print(user.dict())
