# /services – Massimo AI

Questa cartella contiene **tutti i servizi logici** di alto livello che orchestrano le funzioni chiave dell’ecosistema Massimo AI.

Ogni servizio è progettato per:
- **Scalabilità** (puoi splittare in microservizi/domini separati)
- **Sicurezza**
- **Osservabilità e logging**
- **Extensibility** (plugin, automazioni, API)
- **Prontezza cloud**

### Elenco servizi inclusi:
- **factory.py** — AI Factory, generazione mondi verticali
- **ai_engine.py** — Orchestrazione LLM/multimodello, fallback, prompt engineering
- **onboarding.py** — Flusso onboarding, step, quiz, referral, regole mondo
- **analytics.py** — Tracking, KPI, report, esportazione, anomaly detection
- **notification.py** — Notifiche pro, email, SMS, push, batch, priorità
- **payments.py** — Stripe/PayPal, abbonamenti, rimborsi, report, revenue share
- **permissions.py** — Ruoli, permessi, audit, multi-tenant, logging
- **automations.py** — Task, trigger, workflow, AI orchestrazione, scheduler
- **plugins.py** — Sistema plugin, extensibility, API, sicurezza
- **logger.py** — Logging centralizzato, audit, masking, cloud

Tutti i servizi sono già pronti all’uso, facilmente integrabili con API REST/gRPC o estendibili via nuovi provider.
