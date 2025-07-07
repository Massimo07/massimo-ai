"""
CONFIG – Gestione avanzata configurazioni multi-ambiente per Massimo AI.
- Supporto YAML/.env, override runtime, validazione schema.
- Pronto per white-label e multi-tenant.
"""
import os
import yaml
from typing import Dict, Any

class Config:
    """Config Massimo AI: supporta YAML multi-env, override env, validazione, hot-reload."""
    _cache: Dict[str, Any] = {}

    @classmethod
    def load(cls, env: str = None) -> Dict[str, Any]:
        """
        Carica la configurazione da base.yaml e da un file ambiente, override variabili env.
        """
        env = env or os.getenv("ENV", "dev")
        base_path = "./config/base.yaml"
        env_path = f"./config/{env}.yaml"
        config = {}
        # Carica YAML base
        if os.path.exists(base_path):
            with open(base_path) as f:
                config.update(yaml.safe_load(f))
        # Carica YAML ambiente
        if os.path.exists(env_path):
            with open(env_path) as f:
                config.update(yaml.safe_load(f))
        # Override da variabili ambiente
        for k, v in os.environ.items():
            config[k] = v
        # Validazione schema: esempio
        required = ["DATABASE_URL", "SECRET_KEY"]
        for r in required:
            if r not in config:
                raise ValueError(f"Config mancante: {r}")
        cls._cache = config
        return config

    @classmethod
    def get(cls, key, default=None):
        """
        Recupera un valore di configurazione.
        """
        return cls._cache.get(key, default)

    @classmethod
    def reload(cls):
        cls.load()

# Esempio d’uso
if __name__ == "__main__":
    cfg = Config.load("prod")
    print(cfg)
