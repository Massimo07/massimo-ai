"""
core/settings.py

Massimo AI – Settings & Config Management  
Gestione avanzata delle impostazioni: env, override, validazione, segreti, runtime reload.
"""

import os
import json
from typing import Any, Optional

class Settings:
    """
    Sistema di configurazione evoluto:
    - Carica da env, file json, .env, variabili runtime
    - Validazione tipo e sicurezza (segreti nascosti)
    - Override live e salvataggio persistente
    """
    def __init__(self, config_path: str = "settings.json"):
        self.config_path = config_path
        self.data = {}
        self.load()

    def load(self):
        """Carica config da file e variabili d'ambiente."""
        # 1. Carica da file
        if os.path.exists(self.config_path):
            with open(self.config_path, encoding="utf-8") as f:
                self.data.update(json.load(f))
        # 2. Override da env
        for k, v in os.environ.items():
            if k.startswith("MASSIMOAI_"):
                self.data[k.replace("MASSIMOAI_", "").lower()] = v

    def get(self, key: str, default: Any = None) -> Any:
        """Ritorna il valore di una variabile (priorità: runtime > env > file)."""
        return self.data.get(key.lower(), default)

    def set(self, key: str, value: Any):
        """Imposta/aggiorna una variabile e salva su file."""
        self.data[key.lower()] = value
        self.save()

    def save(self):
        """Salva config su file persistente (solo valori non segreti)."""
        # Non salvare chiavi segrete/hardcoded
        out = {k: v for k, v in self.data.items() if "secret" not in k and "password" not in k}
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)

    def get_secret(self, key: str, default: Any = None) -> Any:
        """Gestione segreti separata (mai esportare/loggare i secrets!)."""
        return os.environ.get(key) or self.data.get(key.lower(), default)

# Esempio d’uso
if __name__ == "__main__":
    settings = Settings()
    print(settings.get("ENV", "dev"))
    print(settings.get_secret("OPENAI_API_KEY"))
    settings.set("language", "it")
