# BACKEND – Massimo AI

Entrypoint FastAPI + orchestrazione servizi.  
- Espone tutte le API pubbliche/private
- Logging e audit globali
- Healthcheck pronto per deploy cloud/locale
- Modularità: plug&play su agenti, pagamenti, mondi, auto_factory...

---

## Lancio rapido

```bash
uvicorn backend.main_backend:app --reload
