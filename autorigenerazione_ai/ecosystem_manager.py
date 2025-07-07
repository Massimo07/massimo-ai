import json
from datetime import datetime

class AutorigenerazioneManager:
    def __init__(self, rules_file="rules.json", log_file="log_autorigenerazione.json"):
        self.rules = self.load_rules(rules_file)
        self.log_file = log_file

    def load_rules(self, file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    def check_permission(self, user_level):
        # Solo livelli avanzati abilitati all'autorigenerazione!
        return user_level in self.rules.get("livelli_abilitati", [])

    def suggerisci_upgrade(self, user_level, context):
        if not self.check_permission(user_level):
            return {"status": "forbidden", "msg": "Funzione riservata ai livelli avanzati"}
        # Simulazione di suggestion avanzata AI (estendibile!)
        suggestion = {
            "timestamp": str(datetime.now()),
            "tipo": "upgrade_plugin",
            "plugin": context.get("plugin", "unknown"),
            "suggerimento": f"Potresti aggiungere la funzione {context.get('funzione_nuova', 'NUOVA_FUNZIONE')}!"
        }
        self._log(suggestion)
        return suggestion

    def esegui_autoupgrade(self, user_level, context):
        if not self.check_permission(user_level):
            return {"status": "forbidden", "msg": "Funzione riservata ai livelli avanzati"}
        # Qui puoi agganciare codice AI che aggiorna o rigenera un plugin/modulo/corso
        upgrade = {
            "timestamp": str(datetime.now()),
            "tipo": "auto_upgrade",
            "target": context.get("target", "unknown"),
            "azione": context.get("azione", "upgrade_auto"),
            "status": "eseguito"
        }
        self._log(upgrade)
        return upgrade

    def _log(self, data):
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(data, ensure_ascii=False) + "\n")
        except Exception as e:
            print("Log errore:", e)
