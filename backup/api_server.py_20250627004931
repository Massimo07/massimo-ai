from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

import requests

from bs4 import BeautifulSoup

import json

import os

import time

import threading

import logging

import csv

import pandas as pd

BASE_URL = "https://liveonplus.it"

CATALOG_URL = BASE_URL + "/index.php?route=product/category&path=101"  # Cambia per ogni categoria

DATA_JSON = "data/products_full.json"

DATA_CSV = "data/products_full.csv"

DATA_XLSX = "data/products_full.xlsx"

UPDATE_INTERVAL = 3600

logging.basicConfig(filename="logs/scraper_prodotti.log", level=logging.INFO)

def get_all_product_links():

    links = []

    page = 1

    while True:

        url = f"{CATALOG_URL}&page={page}"

        resp = requests.get(url)

        soup = BeautifulSoup(resp.text, "html.parser")

        items = soup.select(".product-layout .caption a")

        if not items:

            break

        for a in items:

            links.append(a["href"])

        page += 1

    return list(set(links))

def get_product_details(product_url):

    resp = requests.get(product_url)

    soup = BeautifulSoup(resp.text, "html.parser")

    try: title = soup.select_one("h1").text.strip()

    except: title = ""

    try: price = soup.select_one(".price-new, .price").text.strip()

    except: price = ""

    try: punti = soup.find(text=lambda t: "punti" in t.lower()).parent.text

    except: punti = ""

    try: desc = soup.select_one("#tab-description").text.strip()

    except: desc = ""

    try: img = soup.select_one(".thumbnails img")["src"]

    except: img = ""

    return {

        "url": product_url,

        "title": title,

        "price": price,

        "punti": punti,

        "desc": desc,

        "img": img

    }

def save_products_multi(products):

    # Salva JSON

    with open(DATA_JSON, "w", encoding="utf-8") as f:

        json.dump(products, f, ensure_ascii=False, indent=2)

    # Salva CSV

    with open(DATA_CSV, "w", encoding="utf-8", newline="") as f:

        writer = csv.DictWriter(f, fieldnames=products[0].keys())

        writer.writeheader()

        writer.writerows(products)

    # Salva Excel

    df = pd.DataFrame(products)

    df.to_excel(DATA_XLSX, index=False)

def scrape_all_products():

    print("🔄 [Scraper Ultra] Avvio scraping prodotti completi...")

    links = get_all_product_links()

    products = []

    for link in links:

        try:

            p = get_product_details(link)

            products.append(p)

            logging.info(f"[OK] {p['title']} ({link})")

        except Exception as e:

            logging.error(f"[ERR] {link}: {e}")

    save_products_multi(products)

    print(f"✅ [Scraper Ultra] Salvati {len(products)} prodotti.")

    print(f"🔗 [Scraper Ultra] Prodotti trovati: {len(products)} (salvati in JSON, CSV, XLSX)")

def start_scraper_prodotti_ultra():

    def run():

        while True:

            try:

                scrape_all_products()

            except Exception as e:

                logging.error(f"[ERR] Scraper prodotti ultra: {e}")

            time.sleep(UPDATE_INTERVAL)

    threading.Thread(target=run, daemon=True).start()
