from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import os
import time
import subprocess
import sys
import threading

def log(msg):
    print(msg, flush=True)

def check_env_vars():
    required_vars = [
        "TELEGRAM_TOKEN",
        "STRIPE_KEY",
        "OPENAI_API_KEY",
        "LIVEONPLUS_USER",
        "LIVEONPLUS_PASSWORD",
        "LIVEON_USER",
        "LIVEON_PASS"
    ]
    missing = []
    for var in required_vars:
        if not os.environ.get(var):
            missing.append(var)
    if missing:
        log("[ERRORE] Variabili .env mancanti:")
        for m in missing:
            log(f" - {m}")
        log("Correggi il file .env e riavvia.")
        sys.exit(1)

def start_process(cmd, name, wait=1):
    log(f"[START] Avvio: {name} ...")
    proc = subprocess.Popen(cmd, shell=True)
    time.sleep(wait)
    if proc.poll() is not None:
        log(f"[ERRORE] {name} NON AVVIATO! (verifica i log)")
    else:
        log(f"[OK] {name} avviato.")
    return proc

def main():
    log("===============================================")
    log("=============== MASSIMO AI AUTO START =========")
    log("===============================================")
    log(time.strftime("Avvio: %d/%m/%Y %H:%M:%S"))

    # Carica variabili d'ambiente dal .env
    try:
        from dotenv import load_dotenv
        load_dotenv()
        log("[OK] Variabili ambiente caricate da .env")
    except ImportError:
        log("[ERRORE] Impossibile importare dotenv. Installa con: pip install python-dotenv")
        sys.exit(1)

    check_env_vars()

    # Avvia scraper prodotti
    proc_prodotti = start_process("python services/scraper_prodotti_ultra.py", "Scraper Prodotti Ultra")
    # Avvia scraper iscritti
    proc_iscritti = start_process("python services/scraper_iscritti_ultra.py", "Scraper Iscritti Ultra")
    # Avvia bot principale
    proc_bot = start_process("python main.py", "MASSIMO AI BOT", wait=2)

    def watch_and_restart(proc, cmd, name):
        while True:
            ret = proc.poll()
            if ret is not None:
                log(f"[ATTENZIONE] {name} si è interrotto (codice {ret}), riavvio tra 5 secondi...")
                time.sleep(5)
                proc = start_process(cmd, name)
            time.sleep(10)

    # Thread di watchdog per ogni processo
    threading.Thread(target=watch_and_restart, args=(proc_prodotti, "python services/scraper_prodotti_ultra.py", "Scraper Prodotti Ultra"), daemon=True).start()
    threading.Thread(target=watch_and_restart, args=(proc_iscritti, "python services/scraper_iscritti_ultra.py", "Scraper Iscritti Ultra"), daemon=True).start()
    threading.Thread(target=watch_and_restart, args=(proc_bot, "python main.py", "MASSIMO AI BOT"), daemon=True).start()

    # Attendi all'infinito
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        log("[CHIUSURA] Interruzione manuale. Sto terminando i processi...")
        for proc in [proc_prodotti, proc_iscritti, proc_bot]:
            try:
                proc.terminate()
            except Exception:
                pass
        log("[FINE] MASSIMO AI arrestato.")

if __name__ == "__main__":
    main()
async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
