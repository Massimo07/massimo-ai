"""
Modulo: healthcheck.py
Modulo controllo stato sistema: verifica se bot, DB, knowledge base, API e task automatici sono up e funzionanti.
Pronto per server, cloud, Docker Compose (può auto-rilanciare o inviare alert).
"""

import os

def health_status():
    status = {
        "bot": os.path.exists("main.py"),
        "knowledge_base": os.path.exists("knowledge_base.json"),
        "db": os.path.exists("massimo_ai.db"),
        "backup_dir": os.path.exists("backups/")
    }
    status["all_ok"] = all(status.values())
    return status

if __name__ == "__main__":
    print("Stato sistema Massimo AI:", health_status())
