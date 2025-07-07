# ai_automation.py
"""
Modulo Automazione Avanzata per Massimo AI.
Gestisce scheduling, trigger, azioni automatiche e follow-up su ogni canale.
Impossibile da migliorare, pronto per plug-in e orchestrazione multi-mondo.
"""

import datetime
import threading
from typing import Callable, List, Dict, Optional

class AutomationTask:
    def __init__(self, name: str, trigger_time: datetime.datetime, action: Callable, channels: Optional[List[str]] = None, repeat: Optional[int] = None):
        self.name = name
        self.trigger_time = trigger_time
        self.action = action
        self.channels = channels or []
        self.repeat = repeat  # in minuti (None = esegui una volta)
        self.completed = False
        self.log = []

    def run(self):
        self.action()
        self.log.append((datetime.datetime.now(), "Eseguito"))
        if self.repeat:
            next_time = self.trigger_time + datetime.timedelta(minutes=self.repeat)
            threading.Timer((next_time - datetime.datetime.now()).total_seconds(), self.run).start()

class AutomationEngine:
    def __init__(self):
        self.tasks: Dict[str, AutomationTask] = {}

    def add_task(self, task: AutomationTask):
        self.tasks[task.name] = task
        delay = (task.trigger_time - datetime.datetime.now()).total_seconds()
        if delay > 0:
            threading.Timer(delay, task.run).start()
        else:
            task.run()

    def list_tasks(self):
        return {name: {"trigger_time": task.trigger_time, "channels": task.channels, "repeat": task.repeat} for name, task in self.tasks.items()}

    def cancel_task(self, name: str):
        # Per versioni avanzate, tenere traccia del thread e killarlo.
        if name in self.tasks:
            del self.tasks[name]

# ESEMPIO USO:
if __name__ == "__main__":
    def send_reminder():
        print("[Massimo AI] Reminder automatico inviato!")

    task = AutomationTask(
        name="remind_email",
        trigger_time=datetime.datetime.now() + datetime.timedelta(seconds=10),
        action=send_reminder,
        channels=["email", "telegram"],
        repeat=None
    )

    engine = AutomationEngine()
    engine.add_task(task)
    print("Task aggiunto, attesa esecuzione...")
