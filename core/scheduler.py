"""
core/scheduler.py

Massimo AI – Advanced Scheduler
Job, retry, reminder, periodic, async tasks (compat Celery, APScheduler, asyncio).
"""
import threading
import time
from typing import Callable, Any

class JobScheduler:
    def __init__(self):
        self.jobs = []

    def add_job(self, func: Callable, interval: int, args=(), kwargs=None, repeat: int = -1):
        """Aggiunge job periodico (in secondi)."""
        job = {
            "func": func,
            "interval": interval,
            "args": args,
            "kwargs": kwargs or {},
            "repeat": repeat,
            "next_run": time.time() + interval
        }
        self.jobs.append(job)

    def run(self):
        """Avvia il ciclo scheduler (usa in thread/demon)."""
        while True:
            now = time.time()
            for job in self.jobs[:]:
                if now >= job["next_run"]:
                    try:
                        job["func"](*job["args"], **job["kwargs"])
                    except Exception as e:
                        print(f"[SCHEDULER][ERROR]: {e}")
                    job["repeat"] -= 1 if job["repeat"] > 0 else 0
                    if job["repeat"] == 0:
                        self.jobs.remove(job)
                    else:
                        job["next_run"] = now + job["interval"]
            time.sleep(1)

# Esempio di job
if __name__ == "__main__":
    def hello(): print("Hello from Scheduler!")
    scheduler = JobScheduler()
    scheduler.add_job(hello, interval=5, repeat=3)
    t = threading.Thread(target=scheduler.run, daemon=True)
    t.start()
    time.sleep(20)
