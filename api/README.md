# API – Massimo AI

API RESTful per orchestrare, monitorare e automatizzare tutte le funzionalità avanzate del sistema Massimo AI.  
Ogni endpoint è versionato, loggato, spiegato (“explainability”) e pronto per audit/AI Act.

---

## 🚦 Versioning & Modularità
- Tutti gli endpoint sono accessibili su `/api/v1/`
- Ogni microservizio ha test e docstring auto-generati
- Plug-in REST e rotte dinamiche (vedi `plugins.py`)

---

## 🔐 Sicurezza
- JWT/OAuth2, token rotanti, blacklist nativa
- Rate-limiting, CORS, logging tentativi falliti
- Audit trail automatico (ogni azione utente/AI)

---

## 🧠 Explainability
- Ogni risposta critica include spiegazione motivata (“perché”/“come”)
- Audit per AI Act e trasparenza totale

---

## 🛠️ Esempi chiamata

```bash
# Elenco utenti
curl -X GET http://localhost:8000/api/v1/users

# Invia feedback
curl -X POST http://localhost:8000/api/v1/feedback -d '{"user_id":42,"text":"Grande AI!"}'

# Esporta analytics
curl -X GET http://localhost:8000/api/v1/analytics?event_type=payment
