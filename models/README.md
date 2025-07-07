# MODELS – Massimo AI

Modelli dati tipizzati, auditabili, “ready for AI, API, ORM, GDPR”.
- Compatibili Pydantic/FastAPI e SQLAlchemy/ORM
- Ogni modello ha descrizione, validazione, export, history/audit (dove serve)
- Pronti per serialization su API e DB
- Estensione: puoi aggiungere meta, custom_data, versioning

---

## Esempio uso

```python
from models.user import User
from models.subscription import Subscription

user = User(id=1, nome="Mario", email="demo@mail.com")
sub = Subscription(user_id=1, livello="Guida del Team")
print(user, sub)
