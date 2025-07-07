from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_user
import requests
from bs4 import BeautifulSoup
import json
import time
import threading
import logging
import csv
import pandas as pd
from telegram.ext import CommandHandler, ContextTypes

# Inserisci qui le costanti di scraping
DATA_JSON = "data/iscritti_full.json"
DATA_CSV = "data/iscritti_full.csv"
DATA_XLSX = "data/iscritti_full.xlsx"
UPDATE_INTERVAL = 3600

logging.basicConfig(filename="logs/scraper_iscritti.log", level=logging.INFO)

def login_and_get_iscritti():
    # --- IMPLEMENTA QUI LO SCRAPER DI LOGIN CON CREDENZIALI .env ---
    iscritti = []
    # Dummy demo: sostituire con scraping reale!
    for i in range(1, 10):
        iscritti.append({
            "nome": f"Nome{i}",
            "cognome": f"Cognome{i}",
            "codice": f"LOP0000{i}",
            "provincia": "PA",
            "città": "Palermo",
            "telefono": "3200000000"
        })
    return iscritti

def save_iscritti_multi(iscritti):
    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(iscritti, f, ensure_ascii=False, indent=2)
    with open(DATA_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=iscritti[0].keys())
        writer.writeheader()
        writer.writerows(iscritti)
    df = pd.DataFrame(iscritti)
    df.to_excel(DATA_XLSX, index=False)

def scrape_all_iscritti():
    print("🔄 [Scraper Ultra] Avvio scraping iscritti completi...")
    iscritti = login_and_get_iscritti()
    save_iscritti_multi(iscritti)
    print(f"✅ [Scraper Ultra] Salvati {len(iscritti)} iscritti.")
    print(f"🔗 [Scraper Ultra] Iscritti trovati: {len(iscritti)} (salvati in JSON, CSV, XLSX)")

def start_scraper_iscritti_ultra():
    def run():
        while True:
            try:
                scrape_all_iscritti()
            except Exception as e:
                logging.error(f"[ERR] Scraper iscritti ultra: {e}")
            time.sleep(UPDATE_INTERVAL)
    threading.Thread(target=run, daemon=True).start()

# Handler per il bot
async async def command_scraper_iscritti(update, context):
    start_scraper_iscritti_ultra()
    await update.message.reply_text("Scraper iscritti ultra AVVIATO!")

scraper_iscritti_handler = CommandHandler("scraper_iscritti", command_scraper_iscritti)
