# AUTO_FACTORY – Massimo AI

Modulo “plug-and-play” per la **clonazione intelligente** di agenti (AI e umani) o qualsiasi oggetto digitale.
- **Audit trail** e versioning su ogni clone (parent, user, timestamp, versione)
- **Plug-in ready**: basta aggiungere nuovi tipi di entità
- **Security**: puoi tracciare chi clona cosa, pronto per compliance
- **Batch ready**: puoi clonare intere liste (batch)
- Pronto per produzione (logging, test automatici, estensione)

---

## Esempio utilizzo rapido

```python
from auto_factory.clone_agent import clone_agent

agente = {"id": "001", "nome": "Mentor", "personality": "coach", "history": []}
clonato = clone_agent(agente, by_user="mario")
print("Clonato:", clonato)
