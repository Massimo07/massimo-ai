# scraper_ultra.py
"""
Scraper Ultra Massimo AI: login automatico, esplora tutto il sito Live On Plus e salva ogni dato utile.
Salva in /data/scraping/YYYYMMDD_HHMM/ in tutti i formati: .txt, .csv, .json, .md, .html
Esegue scraping ogni 3 ore (immediato al primo run). Ultra robusto, perfetto per automazioni!
"""

import os
from dotenv import load_dotenv
load_dotenv()

import time
import datetime
import requests
import json
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler

# ---- CONFIGURAZIONI ----
LOGIN_URL = "https://liveonplus.it/index.php?route=account/login"
ROOT_URL = "https://liveonplus.it/"
USERNAME = os.getenv("LIVEONPLUS_USER")
PASSWORD = os.getenv("LIVEONPLUS_PASSWORD")
CHROMEDRIVER_PATH = "chromedriver.exe"  # Assicurati che sia nella cartella o nel PATH

SAVE_ROOT = os.path.join("data", "scraping")

# ---- UTILS ----
def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def nowdir():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M")

def get_driver():
    svc = Service(executable_path=CHROMEDRIVER_PATH)
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    # opts.add_argument("--disable-blink-features=AutomationControlled")
    return webdriver.Chrome(service=svc, options=opts)

def login(driver):
    print("DEBUG LOGIN:", USERNAME, PASSWORD)
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
    driver.find_element(By.NAME, "email").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    # Attendi login, verifica presenza di logout/profilo
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='logout']")))
    print("Login OK!")

def save_txt(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def save_csv(path, data, header=None):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(data)

def save_html(path, html):
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

def save_md(path, markdown):
    with open(path, "w", encoding="utf-8") as f:
        f.write(markdown)

def dump_all_formats(basename, content, extra_data=None):
    # Salva lo stesso dato in tutti i formati richiesti
    save_txt(basename + ".txt", content)
    if extra_data:
        save_json(basename + ".json", extra_data)
        if isinstance(extra_data, list) and extra_data and isinstance(extra_data[0], dict):
            save_csv(basename + ".csv", [list(x.values()) for x in extra_data], header=list(extra_data[0].keys()))
    save_md(basename + ".md", f"```\n{content}\n```")
    save_html(basename + ".html", content)

def scrape_product_categories(driver, outdir):
    """Scrape categorie prodotti (puoi aggiungere altre funzioni simili per ogni sezione!)"""
    print("Scraping categorie prodotti...")
    driver.get(ROOT_URL)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    categories = []
    for a in soup.select("a[href*='route=product/category']"):
        name = a.text.strip()
        url = a['href']
        img = ""
        img_tag = a.find("img")
        if img_tag:
            img = img_tag.get("src")
        if name and url:
            categories.append({"name": name, "url": url, "img": img})
    dump_all_formats(os.path.join(outdir, "categorie_prodotti"), json.dumps(categories, ensure_ascii=False), categories)
    print(f"Trovate {len(categories)} categorie prodotti.")
    return categories

def scrape_protected_page(driver, url, outdir, label):
    """Scarica e salva tutto il contenuto di una pagina privata/dettaglio"""
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    dump_all_formats(os.path.join(outdir, label), html)

# --------------- MAIN LOGICA SCRAPER ---------------

def run_scraper():
    print("\nSCRAPER ULTRA attivo (ogni 3 ore, anche ora)")
    now = nowdir()
    outdir = os.path.join(SAVE_ROOT, now)
    ensure_dir(outdir)
    driver = get_driver()
    try:
        login(driver)
        # --- Scraping prodotti base
        categories = scrape_product_categories(driver, outdir)
        # --- Espandi qui: scraping per ogni sezione, area riservata, pdf, info extra, ecc!
        # Ad esempio, per ogni categoria visita la pagina dettagli:
        for cat in categories:
            label = "dettaglio_" + cat["name"].replace(" ", "_").replace("/", "_")
            scrape_protected_page(driver, cat["url"], outdir, label)
        # --- Aggiungi qui scraping documenti PDF, info marketing, area profilo ecc!
        print("Scraping completato e salvato in:", outdir)
    except Exception as e:
        print("ERRORE SCRAPING:", e)
    finally:
        driver.quit()

# ----------- SCHEDULER: ogni 3 ore -----------

def schedule_scraper():
    sched = BlockingScheduler()
    sched.add_job(run_scraper, "interval", hours=3, id="scraper_ultra", next_run_time=datetime.datetime.now())
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scraper Ultra terminato.")

if __name__ == "__main__":
    run_scraper()         # Run subito
    schedule_scraper()    # Ogni 3 ore
