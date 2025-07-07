import asyncio
import logging

class ServiceHealthMonitor:
    def __init__(self, services):
        self.services = services

    async def monitor(self):
        while True:
            for svc in self.services:
                if not await svc.health_check():
                    logging.warning(f"Service {svc.name} unhealthy! Attempting auto-repair...")
                    if not await svc.auto_repair():
                        logging.error(f"Service {svc.name} failed to recover! Founder alerted.")
                        await self.notify_founder(svc.name)
            await asyncio.sleep(10)

    async def notify_founder(self, name):
        from utils.notifier import send_telegram
        await send_telegram(
            token="YOUR_BOT_TOKEN",
            chat_id="FOUNDER_CHAT_ID",
            text=f"[ALERT] {name} irrecuperabile! Intervento manuale necessario."
        )

# Esempio Service:
class ExampleService:
    name = "AI Engine"
    async def health_check(self):
        # Qui test reale: ping, query, chiamata API ecc.
        return True
    async def auto_repair(self):
        # Restart, failover, reload, ecc.
        return True

# Avvio (in main.py o dove vuoi)
# monitor = ServiceHealthMonitor([ExampleService(), ...])
# asyncio.create_task(monitor.monitor())
