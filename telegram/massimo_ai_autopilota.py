from telegram.ext import CommandHandler
import os
import sys
import subprocess
import time
import shutil
import re
from datetime import datetime

# ===============================
# Configura qui il tuo Telegram ID!
TELEGRAM_ID = "5783601920"
# SUGGERIMENTO: il TOKEN lo prende da .env, non lo scrivere in chiaro!
# ===============================

# 1. Backup automatico dei file critici
def backup_files():
    files = ["main.py", "handlers.py", "requirements.txt", ".env"]
    for f in files:
        if os.path.exists(f):
            shutil.copy2(f, f"{f}.bak")

# 2. Check librerie & installazione
REQUIRED_LIBS = [
    "python-telegram-bot==22.1",
    "flask==3.0.3",
    "stripe==12.2.0",
    "openai==1.30.1",
    "apscheduler==3.10.4",
    "python-dotenv==1.0.1",
    "SQLAlchemy==2.0.30",
    "unittest2==1.1.0",
    "scikit-learn==1.4.2",
    "transformers==4.41.2",
    "requests==2.31.0",
    "beautifulsoup4==4.12.3",
    "selenium==4.21.0",
    "reportlab==4.1.0",
    "PyPDF2==3.0.1",
    "Pillow==10.3.0",
    "pandas==2.2.2",
    "numpy==1.26.4",
    "SpeechRecognition==3.10.1",
    "pyttsx3==2.90",
    "streamlit==1.35.0",
    "tqdm==4.66.4",
    "Werkzeug==3.0.3",
    "aiohttp==3.9.5",
    "qrcode==7.4.2",
    "webpush==1.0.2",
    "pytz==2024.1",
    "lxml==5.2.2"
]

def pip_install_missing():
    for pkg in REQUIRED_LIBS:
        pkg_name = pkg.split("==")[0]
        try:
            __import__(pkg_name)
        except ImportError:
            print(f"[LIB] Installa {pkg} ...")
            subprocess.run([sys.executable, "-m", "pip", "install", pkg])

# 3. Fix automatici file (import, Filters, ContextTypes)
def patch_code_files():
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    code = f.read()
                changed = False
                # Fix "Filters" --> "filters"
                code2 = re.sub(r"from telegram\.ext import Filters", "from telegram.ext import filters", code), ContextTypes
                # Fix ContextTypes missing
                code2 = re.sub(r"from telegram\.ext import (.*)", r"from telegram.ext import \1, ContextTypes", code2), ContextTypes
                # Evita doppioni
                code2 = re.sub(r", ContextTypes", ", ContextTypes", code2)
                if code != code2:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(code2)
                    changed = True
                if changed:
                    print(f"[PATCH] {file} patchato.")

# 4. Patch .env con tutte le chiavi fondamentali
ENV_KEYS = {
    "TELEGRAM_TOKEN": "",
    "STRIPE_SECRET_KEY": "",
    "STRIPE_PUB_KEY": "",
    "LIVEON_USER": "",
    "LIVEON_PASS": "",
    "LIVEONPLUS_USER": "",
    "LIVEONPLUS_PASSWORD": ""
}

def fix_env():
    # Leggi .env
    lines = []
    env_vars = {}
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            lines = f.readlines()
    for l in lines:
        if "=" in l:
            k, v = l.strip().split("=", 1)
            env_vars[k] = v
    changed = False
    # Aggiungi chiavi mancanti
    for k, default in ENV_KEYS.items():
        if k not in env_vars or not env_vars[k].strip():
            val = input(f"Inserisci valore per {k} (default '{default}'): ") or default
            env_vars[k] = val
            changed = True
    if changed or not lines:
        with open(".env", "w", encoding="utf-8") as f:
            for k, v in env_vars.items():
                f.write(f"{k}={v}\n")
        print("[.env] File aggiornato!")

def get_telegram_token():
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for l in f:
                if l.strip().startswith("TELEGRAM_TOKEN="):
                    return l.strip().split("=", 1)[1]
    return None

# 5. Avvio dei due scraper (in background) + main.py con restart
def run_scraper_and_main():
    # Scraper prodotti
    try:
        print("[START] Avvio: Scraper Prodotti Ultra ...")
        subprocess.Popen([sys.executable, "services/scraper_prodotti_ultra.py"])
    except Exception as e:
        print(f"[ERR] Scraper prodotti non avviato: {e}")
    # Scraper iscritti
    try:
        print("[START] Avvio: Scraper Iscritti Ultra ...")
        subprocess.Popen([sys.executable, "services/scraper_iscritti_ultra.py"])
    except Exception as e:
        print(f"[ERR] Scraper iscritti non avviato: {e}")
    # Avvio main in loop
    while True:
        try:
            print("[START] Avvio: MASSIMO AI BOT ...")
            subprocess.run([sys.executable, "main.py"], check=True)
        except Exception as e:
            print(f"[BOT ERROR] MASSIMO AI si è fermato: {e}")
            send_telegram_msg("❌ Massimo AI si è fermato! Errore: " + str(e))
            time.sleep(5)

# 6. Invio Telegram
def send_telegram_msg(msg):
    token = get_telegram_token()
    if not token or not TELEGRAM_ID or token.startswith("INSERISCI"):
        return
    import requests
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_ID, "text": msg})

if __name__ == "__main__":
    print("===============================================")
    print("====  MASSIMO AI AUTO PILOTA  =================")
    print("===============================================")
    print(f"Avvio: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    backup_files()
    print("🔄 Backup automatici completati.")
    pip_install_missing()
    print("✅ Librerie installate e aggiornate.")
    patch_code_files()
    print("✅ Codice patchato (import, Filters, ContextTypes).")
    fix_env()
    print("✅ File .env completo e corretto.")
    send_telegram_msg("🚀 Massimo AI: Avvio completato! Sei online, Massimo!")
    run_scraper_and_main()
async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
