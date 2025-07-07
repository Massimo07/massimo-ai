# DEPLOYMENT – Massimo AI

Tutti gli strumenti per deploy cloud, locale, test automatici, backup, scaling.

- **Dockerfile**: builda tutto (backend, worker, frontend se vuoi)
- **docker-compose.yaml**: multi-container (backend, DB, redis, servizi extra)
- **railway.json/render.yaml**: ready per deploy “zero click” su Railway/Render
- **github-actions.yml**: test, build, deploy automatico
- **env.example**: esempio di variabili, DA NON committare mai dati reali!
- **backup.sh**: script rapido backup database + dati
- **entrypoint.sh**: init ambiente (migrate, create superuser, healthcheck…)

---

## Esempio avvio rapido (docker-compose)
```bash
docker-compose up --build
