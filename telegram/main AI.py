"""
main.py — Entrypoint Massimo AI.
Avvia il bot Telegram, gestisce routing handler, automazioni, onboarding, livelli, notifiche.
Pronto per cloud/local, logging, debug, scheduling.
"""

import logging
from telegram.ext import ApplicationBuilder
import config
from handlers import get_handlers
from automation import start_scheduler
from drip_automation import start_scheduler as drip_start
from auto_task import schedule_all_auto_tasks

logging.basicConfig(level=config.LOG_LEVEL)

def main():
    # Avvia gli scheduler per automazioni e drip campaign
    start_scheduler()
    drip_start()

    # Crea l'app Telegram e registra tutti gli handler
    application = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()
    for handler in get_handlers():
        application.add_handler(handler)

    # Schedula i task automatici (auto_task)
    schedule_all_auto_tasks(application.job_queue)

    print("🚀 Massimo AI avviato!")
    application.run_polling()

if __name__ == "__main__":
    main()
