import os
import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from apscheduler.schedulers.background import BackgroundScheduler

BASE_URL = "https://liveonplus.it"
CATALOGHI = [
    "/index.php?route=product/category&path=101",
    "/index.php?route=product/category&path=99",
    # Estendi a tutte le categorie che vuoi!
]

def login_liveonplus():
    from dotenv import load_dotenv
    load_dotenv()
    user = os.getenv("LIVEONPLUS_USER")
    pwd = os.getenv("LIVEONPLUS_PASSWORD")
    svc = Service(executable_path="chromedriver.exe")
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=svc, options=opts)
    driver.get(f"{BASE_URL}/index.php?route=account/login")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(pwd)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)
    return driver

def scrape_categoria(url, driver=None):
    prodotti = []
    if driver:
        driver.get(url)
        html = driver.page_source
    else:
        html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    for box in soup.select("div.product-layout"):
        nome = box.select_one("div.caption a").text.strip()
        link = BASE_URL + box.select_one("div.caption a")["href"]
        prezzo = box.select_one("span.price").text.strip() if box.select_one("span.price") else ""
        img = box.select_one("img")["src"] if box.select_one("img") else ""
        descrizione = ""
        try:
            if driver:
                driver.get(link)
                time.sleep(1)
                detail_soup = BeautifulSoup(driver.page_source, "html.parser")
            else:
                detail_html = requests.get(link).text
                detail_soup = BeautifulSoup(detail_html, "html.parser")
            descr = detail_soup.select_one("div#tab-description")
            descrizione = descr.text.strip() if descr else ""
        except Exception as e:
            descrizione = ""
        prodotti.append({
            "nome": nome,
            "prezzo": prezzo,
            "img": img,
            "link": link,
            "descrizione": descrizione
        })
    return prodotti

def full_scraping():
    print("🔎 [Scraper] Avvio scraping prodotti LiveOnPlus...")
    try:
        driver = login_liveonplus()
        all_prodotti = []
        for path in CATALOGHI:
            print(f"   → Scraping: {path} ...")
            prodotti = scrape_categoria(BASE_URL + path, driver)
            all_prodotti.extend(prodotti)
        driver.quit()
        out_dir = os.path.join(os.path.dirname(__file__), "../data")
        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, "prodotti_liveonplus.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(all_prodotti, f, ensure_ascii=False, indent=2)
        print(f"✅ Scraping completato: {len(all_prodotti)} prodotti salvati.")
    except Exception as e:
        print(f"❌ Errore scraping: {e}")

def schedule_scraping():
    # Primo scraping subito, poi ogni ora
    scheduler = BackgroundScheduler()
    scheduler.add_job(full_scraping, "interval", hours=1, next_run_time=None)
    full_scraping()
    scheduler.start()
