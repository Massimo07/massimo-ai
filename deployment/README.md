# DEPLOYMENT – Massimo AI

Tutto per il deploy cloud, locale, test automatici e backup.

**Avvio rapido:**
- `docker-compose up --build`
- Deploy su Railway/Render: importa repo, setta env, build = entrypoint.sh

**Sicurezza:**  
.env vero NON va mai su repo pubblico!

**Backup:**  
Lancia `backup.sh` per salvataggio rapido DB.

**CI/CD:**  
Ogni push fa test e build automatico (GitHub Actions).
