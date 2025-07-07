
---

# **14. script_bootstrap.py**  
*(Setup semi-automatico per ambienti nuovi/local/dev; crea cartelle, knowledge base, backup, .env template…)*

```python
"""
script_bootstrap.py
Esegue setup ambiente per Massimo AI: crea knowledge_base.json, cartella backup, file .env.example, struttura base plugin.
Perfetto per iniziare in 10 secondi.
"""

import os
import json

dirs = ["backups", "plugins"]
files = {
    "knowledge_base.json": {"products": [], "faq": [], "motivation": []},
    ".env.example": """OPENAI_API_KEY=
TELEGRAM_TOKEN=
STRIPE_SECRET_KEY=
DATABASE_URL=sqlite:///massimo_ai.db
ADMIN_EMAIL=
ADMIN_PASSWORD=
DEBUG=True
LOG_LEVEL=DEBUG
DEFAULT_LANGUAGE=it
ALLOWED_LANGUAGES=it,en,fr,es,de,ro
PROJECT_NAME=Massimo AI
OWNER=Massimo Marfisi
SUPPORT_EMAIL=massimo.ai.official@gmail.com
"""
}

def setup():
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
    for fname, content in files.items():
        if not os.path.exists(fname):
            with open(fname, "w") as f:
                if fname.endswith(".json"):
                    json.dump(content, f, indent=2)
                else:
                    f.write(content)
    print("Bootstrap Massimo AI completato!")

if __name__ == "__main__":
    setup()
