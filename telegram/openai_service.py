# -*- coding: utf-8 -*-
"""Massimo AI – revisione 19 giugno 2025

File openai_service.py — Versione completa e robusta (con scraping multi-thread)

• Web-scraper ESTESO (quick‑view first → fallback Selenium full‑page)
• Gestione persistente dei dati prodotti in SQLite
• Funzione get_openai_response pronta per gli handler Telegram
• **NUOVO:** Scraping multi-thread e estrazione campi avanzati
• **NUOVO:** Esportazione CSV e XLSX
"""

from __future__ import annotations

import atexit
import logging
import os
import re
import sqlite3
import time
import json
import csv
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional, Set
from concurrent.futures import ThreadPoolExecutor, as_completed # Per multi-threading

import requests
from bs4 import BeautifulSoup, FeatureNotFound
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException, StaleElementReferenceException, NoSuchElementException
import pandas as pd # Per esportazione Excel

from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

# ---------------------------------------------------------------------------
# Configurazione (via env‑vars o config.py)
# ---------------------------------------------------------------------------
try:
    from config import (
        OPENAI_API_KEY,
        DATA_PATH,
        DB_PATH,
        VECTOR_INDEX_PATH,
    )
except ImportError:
    logging.warning("File config.py non trovato. Uso variabili ambiente.")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    DATA_PATH = Path(os.getenv("DATA_PATH", "data"))
    DB_PATH = Path(os.getenv("DB_PATH", "massimo.db"))
    VECTOR_INDEX_PATH = Path(os.getenv("VECTOR_INDEX_PATH", "faiss_index/index"))

LIVEONPLUS_USER = os.getenv("LOP_USER", "maxmarfisi@gmail.com")
LIVEONPLUS_PWD = os.getenv("LOP_PWD", "Ma551m07.")
LOGIN_URL = "https://liveonplus.it/index.php?route=account/login"
BASE_URL = "https://liveonplus.it/" # Aggiunto per il crawling delle categorie

# Lista di URL di CATEGORIA principali da cui partire per il crawling ricorsivo (ampliata)
# NOTA: Queste URL vengono usate come PUNTI DI PARTENZA. Lo scraper cercherà automaticamente tutte le altre categorie
# e prodotti a partire dalla homepage e da queste, rendendo questa lista meno critica ma comunque utile.
CATEGORY_URLS = [
    "https://liveonplus.it/index.php?route=product/category&path=99", # Profumi "PECCATI OLFATTIVI"
    "https://liveonplus.it/index.php?route=product/category&path=126", # Cura Corpo "NUOVA SKIN"
    "https://liveonplus.it/index.php?route=product/category&path=156", # Cura Capelli "NUOVA SKIN"
    "https://liveonplus.it/index.php?route=product/category&path=183", # Make Up "MYCOS"
    "https://liveonplus.it/index.php?route=product/category&path=230", # Hair Extetion "CAPELLO PIU' "
    "https://liveonplus.it/index.php?route=product/category&path=243", # Make Up Exclusive " ELITE"
    "https://liveonplus.it/index.php?route=product/category&path=120", # Detergenza Casa "LUCCICA"
    "https://liveonplus.it/index.php?route=product/category&path=229", # Profumatori Casa
    "https://liveonplus.it/index.php?route=product/category&path=221", # Integrazione "INTEGRAMI"
    "https://liveonplus.it/index.php?route=product/category&path=275", # Promozioni
    "https://liveonplus.it/index.php?route=product/category&path=92", # Monodosi
    "https://liveonplus.it/index.php?route=product/category&path=286", # Store Plus
]

WAIT_MAX = 30 # Timeout massimo per le attese di Selenium
SCROLL_PAUSE = 1.5 # Pausa tra gli scroll per caricare contenuti dinamici

# Selettori CSS per identificare i "contenitori" dei prodotti e delle categorie
SEL_PROD = (
    "div.product-thumb, div.product-layout, div.product-item, .product-box, div[class*='product-'], "
    "li.product-grid-item, div.tile.product, div.product-card, div.col-product, "
    "div.product-grid > div, div.row.product-items > div"
)
SEL_CAT = (
    "div.refine-search a[href*='path='], ul.thumbnails a[href*='path='], "
    "div.category-wall a[href*='path='], div.category-list a[href*='path='], "
    "div#content a[href*='path=99_'], div[class*='category-block'] a[href*='path='], "
    "ul.list-group li a[href*='path='], .panel-body a[href*='path='], "
    "div.box-content .list-group a[href*='path=']"
)

# ---------------------------------------------------------------------------
# Logging & DB Setup
# ---------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s") # Impostato a INFO per meno verbosità di default, DEBUG per debugging
log = logging.getLogger("openai_service")

Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# PER FORZARE LA CREAZIONE GIUSTA DELLO SCHEMA:
cur.execute("DROP TABLE IF EXISTS products")
cur.execute("DROP TABLE IF EXISTS messages")
conn.commit()

# Tabella per la cronologia dei messaggi
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        role TEXT,
        content TEXT,
        timestamp TEXT
    )"""
)

# Nuova tabella per i dati dei prodotti (schema espanso)
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS products (
        url TEXT PRIMARY KEY,
        name TEXT,
        price TEXT,
        description TEXT,
        effects_ingredients TEXT,
        code TEXT,
        category TEXT,
        application_area TEXT,
        concerns TEXT,
        image_urls TEXT,
        availability TEXT,
        points TEXT,
        last_updated TEXT
    )"""
)
conn.commit()


def save_message(role: str, content: str) -> None:
    cur.execute(
        "INSERT INTO messages (role, content, timestamp) VALUES (?, ?, ?)",
        (role, content, datetime.utcnow().isoformat()),
    )
    conn.commit()

# ---------------------------------------------------------------------------
# OpenAI / Embeddings / LLM Setup
# ---------------------------------------------------------------------------
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY non configurata – impostare in .env o config.py")

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# ---------------------------------------------------------------------------
# Selenium Driver Management (for scraping)
# ---------------------------------------------------------------------------
# Usiamo una funzione per creare e gestire i driver in modo che ogni thread possa averne uno
def get_new_driver() -> webdriver.Chrome:
    svc = Service(executable_path=str(Path("chromedriver.exe")))
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    opts.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    opts.page_load_strategy = "eager"
    return webdriver.Chrome(service=svc, options=opts)

# Inizializziamo un driver principale per il crawling iniziale delle categorie e dei link
# Gli altri driver verranno creati on-demand nei thread per lo scraping dei dettagli prodotto
main_driver: webdriver.Chrome | None = None
try:
    main_driver = get_new_driver()
    main_driver.implicitly_wait(5)
    log.info("Main WebDriver inizializzato (headless)")
except WebDriverException as e:
    log.error("Selenium non disponibile: %s. Assicurati che chromedriver.exe sia corretto e nel PATH. Lo scraping potrebbe non funzionare.", e)
except Exception as e:
    log.error("Errore generico nell'inizializzazione del Main WebDriver: %s", e)

if main_driver:
    atexit.register(lambda: main_driver.quit()) # Cleanup on exit

# ---------------------------------------------------------------------------
# Utility Functions for Scraping
# ---------------------------------------------------------------------------

def _accept_cookie_if_needed(driver_instance, wait_time=10):
    """Gestisce il banner dei cookie se presente."""
    try:
        cookie_btn = WebDriverWait(driver_instance, wait_time).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'accept') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'accetta')]")
            )
        )
        if cookie_btn:
            cookie_btn.click()
            log.info("Banner cookie accettato.")
            time.sleep(1)
    except TimeoutException:
        pass


def login_if_needed(driver_instance, user=LIVEONPLUS_USER, pwd=LIVEONPLUS_PWD):
    """Esegue il login automatico se non già loggato."""
    if user == "YOUR_LIVEONPLUS_USERNAME" or pwd == "YOUR_LIVEONPLUS_PASSWORD":
        log.warning("[WARN] Credenziali LiveOnPlus non configurate. Lo scraping potrebbe essere limitato o fallire. MODIFICA LIVEONPLUS_USER e LIVEONPLUS_PWD NEL CODICE CON LE TUE CREDENZIALI REALI!")
        return False

    if "account/account" in driver_instance.current_url:
        log.info("Già loggato su LiveOnPlus.")
        return True
    
    try:
        driver_instance.get(LOGIN_URL)
        _accept_cookie_if_needed(driver_instance, wait_time=10)

        WebDriverWait(driver_instance, 20).until(EC.visibility_of_element_located((By.NAME, "email")))
        
        email_input = driver_instance.find_element(By.NAME, "email")
        password_input = driver_instance.find_element(By.NAME, "password")
        submit_button = driver_instance.find_element(By.CSS_SELECTOR, "input[type='submit']")

        email_input.send_keys(user)
        password_input.send_keys(pwd)
        submit_button.click()

        WebDriverWait(driver_instance, 20).until(EC.url_contains("account/account") or EC.url_contains("common/home"))
        
        if "account/account" in driver_instance.current_url or "common/home" in driver_instance.current_url:
            log.info("Login LiveOnPlus riuscito.")
            return True
        else:
            log.error("[ERROR] Login fallito: Reindirizzamento inatteso dopo il submit.")
            return False

    except TimeoutException:
        log.error("[ERROR] Timeout durante il login. Credenziali errate o pagina bloccata. Verifica username/password.")
        return False
    except Exception as e:
        log.error(f"[ERROR] Errore durante il login: {e}")
        return False


def _soup(html: str) -> BeautifulSoup:
    try:
        return BeautifulSoup(html, "lxml")
    except FeatureNotFound:
        return BeautifulSoup(html, "html.parser")


def _to_qv(url: str) -> str:
    m = re.search(r"product_id=(\d+)", url)
    return (
        f"https://liveonplus.it/index.php?route=product/quickview&product_id={m.group(1)}" if m else url
    )


def infer_area_and_concerns(category_name: str, product_name: str, product_description: str) -> Tuple[str, List[str]]:
    """Dedotta l'area di applicazione e i 'concerns' del prodotto.
    (Versione estesa per migliore classificazione)
    """
    text_to_analyze = (category_name + " " + product_name + " " + product_description).lower()
    
    application_area = 'generic'
    if any(keyword in text_to_analyze for keyword in ['capelli', 'hair', 'shampoo', 'maschera capillare', 'balsamo', 'cuoio capelluto', 'capillare']):
        application_area = 'hair'
    elif any(keyword in text_to_analyze for keyword in ['viso', 'face', 'crema viso', 'siero', 'trucco', 'make up', 'contorno occhi', 'maschera viso', 'dermica', 'facciale']):
        application_area = 'face'
    elif any(keyword in text_to_analyze for keyword in ['corpo', 'body', 'crema corpo', 'bagnoschiuma', 'doccia', 'solare', 'abbronzante', 'gambe', 'mani', 'piedi', 'cutanea']):
        application_area = 'body'
    elif any(keyword in text_to_analyze for keyword in ['profumi', 'fragranze', 'olfattivi', 'eau de toilette', 'eau de parfum', 'aroma']):
        application_area = 'perfume'
    elif any(keyword in text_to_analyze for keyword in ['casa', 'detergenza', 'ambiente', 'bucato', 'pulizia']):
        application_area = 'home'
    elif any(keyword in text_to_analyze for keyword in ['integrazione', 'integratori', 'integratore', 'vitaminico', 'nutrizionale']):
        application_area = 'supplements'
    elif any(keyword in text_to_analyze for keyword in ['make up', 'trucco', 'cosmetici', 'ombretto', 'rossetto', 'fondotinta']):
        application_area = 'makeup'


    SKIN_CONCERNS_MAP = {
        "hyperpigmentation": ["macchie", "discromie", "melasma", "iperpigmentazione", "schiarente", "anti-macchia", "uniformante", "tono della pelle"],
        "acne": ["brufoli", "impurità", "acneica", "pelle grassa", "pori dilatati"],
        "aging": ["rughe", "anti-età", "antiage", "invecchiamento", "elasticità", "compattezza"],
        "hydration": ["idratante", "secca", "disidratata", "nutriente", "umettante"],
        "sensitivity": ["sensibile", "arrossamenti", "lenitivo", "irritazioni"],
        "sun_protection": ["solare", "spf", "uva", "uvb", "abbronzante", "protezione solare"],
        "dandruff": ["forfora", "desquamazione", "cuoio capelluto secco"], # for hair
        "hair_loss": ["caduta capelli", "rinforzante capelli", "anticaduta"], # for hair
        "yellow_tones": ["antigiallo", "riflessi gialli", "aranciati"], # for hair
        "blemishes": ["imperfezioni", "rossore"],
        "volume_shine": ["volume", "lucentezza", "brillantezza"], # for hair/makeup
    }
    
    detected_concerns = []
    for concern_type, keywords in SKIN_CONCERNS_MAP.items():
        if any(keyword in text_to_analyze for keyword in keywords):
            detected_concerns.append(concern_type)

    return application_area, detected_concerns

# ---------------------------------------------------------------------------
# Product Detail Parsing (Quick-view and Full-Page Selenium)
# ---------------------------------------------------------------------------

def parse_product_details(prod_url: str) -> Optional[Dict[str, Any]]: # Removed sess, driver will be created per-thread
    """
    Scarica la pagina di un singolo prodotto ed estrae dettagli specifici.
    Tenta prima con quick-view (requests), poi fallback a pagina completa (Selenium) se fallisce.
    Returns a dictionary of product data or None if parsing fails.
    This function will now create its own driver for thread safety.
    """
    local_driver = None # Driver locale per il thread
    try:
        local_driver = get_new_driver() # Ottieni un nuovo driver per questo thread
        local_driver.implicitly_wait(5)
        local_sess = requests.Session() # Sessione requests per questo thread

        # Inseriamo il login qui per ogni driver, così sono indipendenti
        login_if_needed(local_driver)
        # Aggiorniamo i cookie della sessione requests con quelli del driver appena loggato
        for c in local_driver.get_cookies():
            local_sess.cookies.set(c["name"], c["value"], domain="liveonplus.it")
        local_sess.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})


        product_data: Dict[str, Any] = {
            "url": prod_url,
            "name": "N/D",
            "price": "N/D",
            "description": "N/D",
            "effects_ingredients": "N/D",
            "code": "N/D",
            "category": "Non specificata",
            "application_area": "generic",
            "concerns": [],
            "image_urls": [],
            "availability": "N/D",
            "points": "N/D",
        }
        quickview_url = _to_qv(prod_url)
        
        # Tentativo 1: Quick-view via requests (più veloce e leggero)
        try:
            r = local_sess.get(quickview_url, timeout=10)
            r.raise_for_status()
            soup = _soup(r.text)
            
            # AGGIORNATO: Selettori ancora più robusti per i dettagli prodotto (Quick-view)
            name_tag = soup.select_one("h1.product-name, h2.tt-title, h3.name, .product-info h1, .product-main-info h2, .product-title h1, .product-heading, h1, h2, .prodotto h1")
            if name_tag:
                product_data['name'] = name_tag.get_text(" ", strip=True)
            
            price_tag = soup.select_one(".price-new, .price, .tt-price, .product-price, .current-price, .product-info .price, .product-main-info .price, .prezzo")
            if price_tag:
                raw_price = price_tag.get_text(" ", strip=True)
                clean_price_match = re.search(r'[\d\.,]+', raw_price)
                product_data['price'] = clean_price_match.group(0).strip() if clean_price_match else raw_price
            
            code_tag = soup.find(text=lambda s: s and "Product Code" in s) or \
                       soup.find('span', string=re.compile(r'Product Code', re.IGNORECASE)) or \
                       soup.select_one(".model, .product-code, .sku, .product-id-value, .item-code")
            if code_tag:
                code_text = code_tag.get_text(" ", strip=True) if hasattr(code_tag, 'get_text') else code_tag
                match = re.search(r'(?:Product Code|Codice Prodotto|SKU|Cod):\s*([a-zA-Z0-9\-\_]+)', code_text, re.IGNORECASE)
                if match:
                    product_data['code'] = match.group(1).strip()
                else:
                    product_data['code'] = code_text.strip()
            
            category_tag = soup.select_one("ul.breadcrumb li:nth-last-child(2) a, .breadcrumbs a:nth-last-child(2), .breadcrumbs li:nth-last-child(2) a")
            if category_tag:
                product_data['category'] = category_tag.get_text(strip=True)
            
            description_tag = soup.select_one("div#product-description, div.product-description, div.info-text, .tab-content #tab-description, .description-full, .product-summary, .description-block, #description, .product-desc, .desc") or \
                              soup.find('div', class_=re.compile(r'description|detail|tab', re.IGNORECASE))
            if description_tag:
                product_data['description'] = description_tag.get_text(" ", strip=True)
            
            effects_ingredients_tag = soup.select_one("div#product-attribute, div.specifiche, ul.list-unstyled, div.product-details, .tab-content #tab-specification, .attributes-table, #tab-info, .product-features") or \
                                      soup.find('div', class_=re.compile(r'effects|benefits|ingredients|specifiche|caratteristiche|attributi', re.IGNORECASE))
            if effects_ingredients_tag:
                product_data['effects_ingredients'] = effects_ingredients_tag.get_text(" ", strip=True)
            
            # Immagini URL
            image_urls = []
            thumbs = soup.select(".image-additional img, .thumbnails img, .product-images img, .image-thumb img, .gallery-thumbs img, img#image")
            for t in thumbs:
                src = t.get("src")
                if src and "data:image" not in src:
                    image_urls.append(src)
            if not image_urls:
                main_img_tag = soup.select_one(".product-info .image img, .thumbnail img, .main-image img, .product-image-container img, .product-main-image img, .product-image img")
                if main_img_tag:
                    src = main_img_tag.get("src")
                    if src and "data:image" not in src:
                        image_urls.append(src)
            product_data['image_urls'] = image_urls

            availability_tag = soup.select_one(".stock-status, .availability span, .product-stock")
            if availability_tag:
                product_data['availability'] = availability_tag.get_text(" ", strip=True)

            points_tag = soup.find(text=re.compile(r'Punti:?\s*\d+', re.IGNORECASE)) # Cerca "Punti: X" o "Punti X"
            if points_tag:
                product_data['points'] = points_tag.strip()

            if product_data['name'] != "N/D":
                log.debug(f"  Scraped quick-view: {quickview_url}")
                application_area, concerns = infer_area_and_concerns(
                    product_data['category'], product_data['name'], product_data['description']
                )
                product_data['application_area'] = application_area
                product_data['concerns'] = concerns
                return product_data # Return if quick-view successful
            else:
                log.warning(f"Quick-view parsing incomplete for {quickview_url}. Falling back to full page.")
                product_data = {} # Reset to force fallback

        except requests.exceptions.RequestException as e:
            log.warning(f"Requests error for quick-view {quickview_url}: {e}. Falling back to full page.")
            product_data = {} # Reset
        except Exception as e:
            log.warning(f"Error parsing quick-view {quickview_url}: {e}. Falling back to full page.")
            product_data = {} # Reset

        # Tentativo 2: Fallback alla pagina completa via Selenium (se quick-view fallisce)
        if not product_data: # Only proceed with Selenium if product_data is still empty
            try:
                local_driver.get(prod_url)
                _accept_cookie_if_needed(local_driver, wait_time=5)
                # Attesa più generica per la visibilità di un contenitore prodotto
                WebDriverWait(local_driver, WAIT_MAX).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-info, .product-main-info, .product-view, .product-detail, #content, main'))
                )
                soup = _soup(local_driver.page_source)

                # Re-applicare i selettori robusti per il fallback Selenium
                name_tag_selenium = soup.select_one("h1.product-name, h2.tt-title, h3.name, .product-info h1, .product-main-info h2, .product-title h1, .product-heading, h1, h2, .prodotto h1")
                product_data['name'] = name_tag_selenium.get_text(strip=True) if name_tag_selenium else "N/D"
                
                description_container_selenium = soup.select_one("div#product-description, div.product-description, div.info-text, .tab-content #tab-description, .description-full, .product-summary, .description-block, #description, .product-desc, .desc") or \
                                        soup.find('div', class_=re.compile(r'description|product-description|info', re.IGNORECASE))
                if description_container_selenium:
                    product_data['description'] = description_container_selenium.get_text(separator=' ', strip=True)
                else:
                    main_content_selenium = soup.find('div', id=re.compile(r'content|main-content')) or soup.find('main')
                    product_data['description'] = main_content_selenium.get_text(separator=' ', strip=True) if main_content_selenium else "N/D"

                effects_tag_selenium = soup.select_one("div#product-attribute, div.specifiche, ul.list-unstyled, div.product-details, .tab-content #tab-specification, .attributes-table, #tab-info, .product-features") or \
                              soup.find('div', class_=re.compile(r'effects|benefits|ingredients|specifiche|caratteristiche|attributi', re.IGNORECASE))
                if effects_tag_selenium:
                    product_data['effects_ingredients'] = effects_tag_selenium.get_text(separator=' ', strip=True)
                
                price_tag_selenium = soup.select_one(".price-new, .price, .tt-price, .product-price, .current-price, .product-info .price, .product-main-info .price, .prezzo")
                if price_tag_selenium:
                    raw_price = price_tag_selenium.get_text(" ", strip=True)
                    clean_price_match = re.search(r'[\d\.,]+', raw_price)
                    product_data['price'] = clean_price_match.group(0).strip() if clean_price_match else raw_price

                code_tag_selenium = soup.find(text=lambda s: s and "Product Code" in s) or \
                                    soup.find('span', string=re.compile(r'Product Code', re.IGNORECASE)) or \
                                    soup.select_one(".model, .product-code, .sku, .product-id-value, .item-code")
                if code_tag_selenium:
                    code_text = code_tag_selenium.get_text(" ", strip=True) if hasattr(code_tag_selenium, 'get_text') else code_tag_selenium
                    match = re.search(r'(?:Product Code|Codice Prodotto|SKU|Cod):\s*([a-zA-Z0-9\-\_]+)', code_text, re.IGNORECASE)
                    if match:
                        product_data['code'] = match.group(1).strip()
                    else:
                        product_data['code'] = code_text.strip()

                category_name_from_breadcrumb = "Non specificata (FullPage)"
                breadcrumb_selenium = soup.select_one("ul.breadcrumb, nav.breadcrumb, .breadcrumbs")
                if breadcrumb_selenium:
                    category_links = breadcrumb_selenium.find_all("a", href=re.compile(r"path="))
                    if category_links:
                        category_name_from_breadcrumb = category_links[-1].get_text(strip=True)
                product_data['category'] = category_name_from_breadcrumb
                
                # Immagini per Selenium fallback
                image_urls = []
                try:
                    thumbs = local_driver.find_elements(By.CSS_SELECTOR, ".image-additional img, .thumbnails img, .product-images img, .image-thumb img, .gallery-thumbs img, img#image")
                    for t in thumbs:
                        src = t.get_attribute("src")
                        if src and "data:image" not in src:
                            image_urls.append(src)
                except NoSuchElementException:
                    pass
                if not image_urls:
                    try:
                        main_img_el = local_driver.find_element(By.CSS_SELECTOR, ".product-info .image img, .thumbnail img, .main-image img, .product-image-container img, .product-main-image img, .product-image img")
                        src = main_img_el.get_attribute("src")
                        if src and "data:image" not in src:
                            image_urls.append(src)
                    except NoSuchElementException:
                        pass
                product_data['image_urls'] = image_urls

                availability_tag_selenium = soup.select_one(".stock-status, .availability span, .product-stock")
                if availability_tag_selenium:
                    product_data['availability'] = availability_tag_selenium.get_text(" ", strip=True)
                
                points_tag_selenium = soup.find(text=re.compile(r'Punti:?\s*\d+', re.IGNORECASE))
                if points_tag_selenium:
                    product_data['points'] = points_tag_selenium.strip()

                if product_data['name'] != "N/D": # Se almeno il nome è stato estratto con Selenium
                    log.debug(f"  Scraped details from full page: {prod_url}")
                    application_area, concerns = infer_area_and_concerns(
                        product_data['category'], product_data['name'], product_data['description']
                    )
                    product_data['application_area'] = application_area
                    product_data['concerns'] = concerns
                    return product_data # Return if full page successful
                else:
                    log.warning(f"Full page Selenium parsing incomplete for {prod_url}. Saving debug HTML.")
                    # Salvataggio HTML per debug se fallisce completamente
                    product_id = prod_url.split("product_id=")[-1].split("&")[0] if "product_id=" in prod_url else "unknown"
                    debug_file = f"debug_{product_id}.html"
                    with open(debug_file, "w", encoding="utf-8") as f:
                        f.write(local_driver.page_source)
                    log.info(f"Saved debug HTML to {debug_file} for URL: {prod_url}")


            except TimeoutException:
                log.warning(f"Timeout ({WAIT_MAX}s) loading elements for {prod_url}. Returning None.")
                # Salvataggio HTML per debug se timeout
                product_id = prod_url.split("product_id=")[-1].split("&")[0] if "product_id=" in prod_url else "unknown"
                debug_file = f"debug_{product_id}.html"
                with open(debug_file, "w", encoding="utf-8") as f:
                    f.write(local_driver.page_source)
                log.info(f"Saved debug HTML to {debug_file} for URL: {prod_url}")
            except WebDriverException as e:
                log.error(f"Selenium error during download/parsing of {prod_url}: {e}. Returning None. Saving debug HTML.")
                # Salvataggio HTML per debug se WebDriverException
                product_id = prod_url.split("product_id=")[-1].split("&")[0] if "product_id=" in prod_url else "unknown"
                debug_file = f"debug_{product_id}.html"
                with open(debug_file, "w", encoding="utf-8") as f:
                    f.write(local_driver.page_source)
                log.info(f"Saved debug HTML to {debug_file} for URL: {prod_url}")
            except Exception as e:
                log.error(f"Generic error parsing product page {prod_url}: {e}. Returning None. Saving debug HTML.")
                # Salvataggio HTML per debug se errore generico
                product_id = prod_url.split("product_id=")[-1].split("&")[0] if "product_id=" in prod_url else "unknown"
                debug_file = f"debug_{product_id}.html"
                with open(debug_file, "w", encoding="utf-8") as f:
                    f.write(local_driver.page_source)
                log.info(f"Saved debug HTML to {debug_file} for URL: {prod_url}")
    finally:
        if local_driver:
            local_driver.quit() # Assicurati che il driver locale venga chiuso
    
    return None # Return None if all attempts fail


def collect_product_links_recursively(driver_instance: webdriver.Chrome, url: str, seen_urls: Optional[Set[str]] = None) -> Set[str]:
    """Raccoglie ricorsivamente i link dei prodotti e naviga tra categorie/sottocategorie, gestendo la paginazione.
    Restituisce un set di URL di prodotti unici trovati in questa categoria e nelle sue sottocategorie.
    Implementa la logica "intelligente": se trova prodotti in una categoria, colleziona quelli ed evita di scendere in sottocategorie
    DA QUEL PUNTO della ricorsione.
    """
    if seen_urls is None:
        seen_urls = set()

    if url in seen_urls:
        log.debug(f"Skipping already visited URL: {url}")
        return set()
    seen_urls.add(url)
    
    products_found_in_this_category_branch: Set[str] = set()

    try:
        driver_instance.get(url)
        _accept_cookie_if_needed(driver_instance)
        log.info(f"Crawling category: {url}...")

        # Aggiunto un wait più robusto per la pagina di categoria
        WebDriverWait(driver_instance, WAIT_MAX).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"{SEL_PROD}, {SEL_CAT}, .product-grid, .category-info, #content"))
        )

        current_page_product_urls: Set[str] = set()
        
        products_directly_found_on_pages = False
        page_num = 1
        while True:
            log.debug(f"  Attempting to find products on page {page_num} of category: {url}")
            # Re-trova gli elementi dei prodotti ad ogni iterazione della paginazione
            product_elements = driver_instance.find_elements(By.CSS_SELECTOR, f"{SEL_PROD} a[href*='product/product']")
            
            if product_elements:
                products_directly_found_on_pages = True
                for el in product_elements:
                    try:
                        href = el.get_attribute("href")
                        if href and "quickview" not in href and "product_id=" in href: # Assicurati che sia un link prodotto
                            current_page_product_urls.add(href)
                    except StaleElementReferenceException:
                        log.warning(f"Stale element reference for product link on {driver_instance.current_url}. Retrying elements for current page.")
                        pass 
            
            log.debug(f"  Found {len(current_page_product_urls)} product links on current paginated view of {driver_instance.current_url}.")
            
            # Tenta di andare alla pagina successiva
            try:
                pagination_container = WebDriverWait(driver_instance, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination"))
                )
                next_button = pagination_container.find_element(By.CSS_SELECTOR, ".next a, .next_page a, a[rel='next']")
                
                if "disabled" in next_button.get_attribute("class").split() or \
                   not next_button.is_displayed() or \
                   not next_button.is_enabled():
                    log.debug(f"  Next button on {driver_instance.current_url} is disabled or not present. Ending pagination.")
                    break
                
                current_url_before_click = driver_instance.current_url
                driver_instance.execute_script("arguments[0].click();", next_button)
                time.sleep(SCROLL_PAUSE)
                
                WebDriverWait(driver_instance, WAIT_MAX).until(
                    EC.staleness_of(next_button) or EC.url_changes(current_url_before_click)
                )
                page_num += 1
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                log.debug(f"  No next button found or timeout on {driver_instance.current_url}. Ending pagination for this category.")
                break
            except Exception as e:
                log.warning(f"Error during pagination for {driver_instance.current_url}: {e}. Ending pagination.")
                break
        
        products_found_in_this_category_branch.update(current_page_product_urls)

        # LOGICA CRUCIALE: Se abbiamo trovato prodotti direttamente in questa categoria, NON scendiamo in sottocategorie da qui.
        if products_directly_found_on_pages and current_page_product_urls:
            log.info(f"  Category '{url}' contains products ({len(current_page_product_urls)} found). Not descending into subcategories from this branch.")
            return products_found_in_this_category_branch

        log.info(f"  Finished direct product scan for {url}. Total unique products found directly: {len(current_page_product_urls)}. Checking subcategories now.")

        # Se non sono stati trovati prodotti direttamente, allora cerca sottocategorie e ricorsi.
        subcat_elements = driver_instance.find_elements(By.CSS_SELECTOR, SEL_CAT)
        sub_hrefs_to_recurse = []
        for sub_el in subcat_elements:
            href = sub_el.get_attribute("href")
            # FILTRO IMPORTANTE: aggiungi alla lista di ricorsione solo se è un link di categoria, NON un link di prodotto, e non l'URL corrente
            if href and "path=" in href and "product_id=" not in href and href != url:
                 sub_hrefs_to_recurse.append(href)
        
        log.info(f"  Found {len(sub_hrefs_to_recurse)} valid subcategory links on {url}.")

        for sub_href in sub_hrefs_to_recurse:
            products_found_in_this_category_branch.update(collect_product_links_recursively(driver_instance, sub_href, seen_urls))
        
    except TimeoutException:
        log.warning(f"Timeout ({WAIT_MAX}s) for {url}. Page might not have loaded completely or no content found.")
    except Exception as e:
        if isinstance(e, StaleElementReferenceException):
            log.error(f"StaleElementReferenceException (outer loop) while crawling {url}: {e}. This might mean an element used to find subcategories became stale after a page update. Some links might be missed.")
        else:
            log.error(f"Error crawling {url}: {e}")

    return products_found_in_this_category_branch


def _load_products_from_db() -> Dict[str, Dict[str, Any]]:
    """Carica i prodotti esistenti dal database SQLite."""
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    products_from_db = {}
    for row in rows:
        # Converti i dati dal formato di DB al dizionario
        product_dict = {
            "url": row[0],
            "name": row[1],
            "price": row[2],
            "description": row[3],
            "effects_ingredients": row[4],
            "code": row[5],
            "category": row[6],
            "application_area": row[7],
            "concerns": json.loads(row[8]) if row[8] else [],
            "image_urls": json.loads(row[9]) if row[9] else [],
            "availability": row[10], # Nuovo campo
            "points": row[11],       # Nuovo campo
            "last_updated": row[12]
        }
        products_from_db[product_dict['url']] = product_dict
    log.info(f"Caricati {len(products_from_db)} prodotti dal database SQLite.")
    return products_from_db


def _save_product_to_db(product_data: Dict[str, Any]):
    """Salva o aggiorna un singolo prodotto nel database SQLite."""
    product_data['concerns'] = json.dumps(product_data.get('concerns', []))
    product_data['image_urls'] = json.dumps(product_data.get('image_urls', []))
    product_data['last_updated'] = datetime.utcnow().isoformat()

    cur.execute(
        """
        INSERT OR REPLACE INTO products (
            url, name, price, description, effects_ingredients, code, category, 
            application_area, concerns, image_urls, availability, points, last_updated
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            product_data['url'], product_data['name'], product_data['price'], product_data['description'],
            product_data['effects_ingredients'], product_data['code'], product_data['category'],
            product_data['application_area'], product_data['concerns'], product_data['image_urls'],
            product_data['availability'], product_data['points'], product_data['last_updated']
        )
    )
    conn.commit()

def export_products_to_csv_and_excel(output_csv_file: str = "products_export.csv", output_xlsx_file: str = "products_export.xlsx"):
    """Esporta tutti i prodotti dal database SQLite a un file CSV e Excel."""
    log.info(f"Esportazione prodotti in {output_csv_file} e {output_xlsx_file}...")
    products_data = _load_products_from_db()

    if not products_data:
        log.warning("Nessun prodotto trovato nel database da esportare.")
        return

    # Preparare i dati per DataFrame/CSV/Excel
    records_to_export = []
    for product_url, data in products_data.items():
        record = data.copy()
        record['concerns'] = ', '.join(record['concerns']) # Converti lista a stringa per CSV/Excel
        record['image_urls'] = '|'.join(record['image_urls']) # Converti lista a stringa per CSV/Excel
        records_to_export.append(record)

    df = pd.DataFrame(records_to_export)

    # Reorder columns for better readability in output files
    ordered_columns = [
        "name", "price", "description", "effects_ingredients", "code", "category",
        "application_area", "concerns", "availability", "points", "image_urls", "url", "last_updated"
    ]
    # Ensure all ordered_columns exist in the DataFrame, add missing ones as empty if necessary
    for col in ordered_columns:
        if col not in df.columns:
            df[col] = None
    df = df[ordered_columns]

    # Salvataggio su CSV
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=df.columns)
        writer.writeheader()
        for _, row in df.iterrows():
            writer.writerow(row.to_dict())
    log.info(f"Esportazione CSV completata. {len(products_data)} prodotti salvati in {output_csv_file}.")

    # Salvataggio su Excel
    df.to_excel(output_xlsx_file, index=False, engine='openpyxl')
    log.info(f"Esportazione Excel completata. {len(products_data)} prodotti salvati in {output_xlsx_file}.")


# ---------------------------------------------------------------------------
# FAISS Index Build (now loads from DB and updates via scraping)
# ---------------------------------------------------------------------------

def build_vector_store() -> FAISS:
    # 1. Carica i prodotti esistenti dal database
    products_in_db = _load_products_from_db()
    
    new_or_updated_count = 0
    skipped_count = 0

    # 2. Esegui lo scraping per trovare tutti i link e aggiornare il database
    all_scraped_product_urls: Set[str] = set()

    if main_driver: # Esegui crawling dinamico solo se il driver principale è disponibile
        log.info("Attempting login to LiveOnPlus for crawling categories...")
        login_successful = login_if_needed(main_driver)
        if not login_successful:
            log.warning("LiveOnPlus login failed for initial category crawling. Proceeding with limited access.")
        
        # Inizia il crawling dalla homepage per trovare tutte le categorie
        log.info(f"Starting deep crawl from homepage: {BASE_URL}")
        all_scraped_product_urls.update(collect_product_links_recursively(main_driver, BASE_URL))

        for url in CATEGORY_URLS: # Aggiungi anche le CATEGORY_URLS iniziali per sicurezza
            all_scraped_product_urls.update(collect_product_links_recursively(main_driver, url))

        log.info(f"Total unique product URLs collected for detailed scraping: {len(all_scraped_product_urls)}")

        # Elabora ciascun URL di prodotto in parallelo
        log.info("Starting parallel product detail scraping...")
        # Ho impostato 4 workers per non sovraccaricare il sito o il tuo PC, puoi aumentare
        with ThreadPoolExecutor(max_workers=4) as executor: 
            future_to_url = {executor.submit(parse_product_details, p_url): p_url for p_url in all_scraped_product_urls}
            
            for i, future in enumerate(as_completed(future_to_url)):
                p_url = future_to_url[future]
                try:
                    scraped_product_data = future.result()
                    if scraped_product_data:
                        # Check if product is new or needs update
                        db_product = products_in_db.get(p_url)
                        needs_update = False
                        if not db_product:
                            needs_update = True
                        else: # Compare fields to see if update is needed
                            # Need to deserialize concerns/image_urls from DB for comparison
                            db_concerns = json.loads(db_product.get('concerns', '[]'))
                            db_image_urls = json.loads(db_product.get('image_urls', '[]'))

                            if (scraped_product_data.get('name', '').strip() != db_product.get('name', '').strip() or
                                scraped_product_data.get('price', '').strip() != db_product.get('price', '').strip() or
                                scraped_product_data.get('description', '').strip() != db_product.get('description', '').strip() or
                                scraped_product_data.get('effects_ingredients', '').strip() != db_product.get('effects_ingredients', '').strip() or
                                scraped_product_data.get('code', '').strip() != db_product.get('code', '').strip() or
                                scraped_product_data.get('category', '').strip() != db_product.get('category', '').strip() or
                                scraped_product_data.get('application_area', '').strip() != db_product.get('application_area', '').strip() or
                                scraped_product_data.get('availability', '').strip() != db_product.get('availability', '').strip() or # New field
                                scraped_product_data.get('points', '').strip() != db_product.get('points', '').strip() or # New field
                                set(scraped_product_data.get('concerns', [])) != set(db_concerns) or
                                set(scraped_product_data.get('image_urls', [])) != set(db_image_urls)):
                                needs_update = True

                        if needs_update:
                            _save_product_to_db(scraped_product_data)
                            log.info(f"[{i+1}/{len(all_scraped_product_urls)}] Updated/Added product: {scraped_product_data.get('name', p_url)}")
                            products_in_db[p_url] = scraped_product_data # Update in memory for indexing
                            new_or_updated_count += 1
                        else:
                            log.debug(f"[{i+1}/{len(all_scraped_product_urls)}] Product {scraped_product_data.get('name', p_url)} already up-to-date.")
                            skipped_count += 1
                    else:
                        log.warning(f"[{i+1}/{len(all_scraped_product_urls)}] Skipped URL due to parsing failure: {p_url}")
                        skipped_count += 1
                except Exception as e:
                    log.error(f"[{i+1}/{len(all_scraped_product_urls)}] Error processing {p_url}: {e}", exc_info=True)
                    skipped_count += 1

    log.info(f"Finished parallel scraping and database update. New/Updated: {new_or_updated_count}, Skipped/Existing: {skipped_count}.")

    # 3. Costruisci i documenti LangChain dal database completo (sia vecchi che nuovi/aggiornati)
    # Ricarica tutti i prodotti dal DB per essere sicuro di avere la versione più recente e completa
    final_products_for_indexing = _load_products_from_db()
    docs: List[Document] = []
    if final_products_for_indexing:
        for p_data in final_products_for_indexing.values():
            concerns_text = f"Concerns: {', '.join(p_data.get('concerns', []))}\n" if p_data.get('concerns') else ""
            image_urls_text = f"URLs Immagini: {', '.join(p_data.get('image_urls', []))}\n" if p_data.get('image_urls') else ""
            
            content = (
                f"Nome Prodotto: {p_data.get('name', 'Nome non disponibile')}\n"
                f"Categoria: {p_data.get('category', 'Non specificata')}\n"
                f"Area di Applicazione: {p_data.get('application_area', 'Generica')}\n"
                f"{concerns_text}"
                f"Descrizione: {p_data.get('description', 'Descrizione non disponibile')}\n"
                f"Effetti/Ingredienti: {p_data.get('effects_ingredients', 'Effetti/ingredienti non disponibili')}\n"
                f"Prezzo: {p_data.get('price', 'Non disponibile')}\n"
                f"Codice Prodotto: {p_data.get('code', 'Non disponibile')}\n"
                f"Disponibilità: {p_data.get('availability', 'Non disponibile')}\n"
                f"Punti: {p_data.get('points', 'Non disponibile')}\n"
                f"{image_urls_text}"
                f"URL: {p_data.get('url', '')}"
            )
            # Metadati devono essere compatibili con LangChain Document
            metadata = {
                "source": p_data.get('url'),
                "type": "product_detail",
                "name": p_data.get('name'),
                "code": p_data.get('code'),
                "category": p_data.get('category'),
                "application_area": p_data.get('application_area'),
                "concerns": p_data.get('concerns', []), # Store as list in metadata
                "price": p_data.get('price'),
                "availability": p_data.get('availability'), # New metadata
                "points": p_data.get('points'),             # New metadata
                "image_urls": p_data.get('image_urls', []), # Store as list in metadata
                "last_updated": p_data.get('last_updated')
            }
            docs.append(Document(page_content=content, metadata=metadata))
    else:
        log.warning("Nessun documento trovato nel database o dallo scraping. La base di conoscenza dell'AI è vuota.")
        docs.append(
            Document(
                page_content="Massimo AI: Nessun documento fornito o indicizzato. Per maggiori informazioni, fornire file PDF/CSV/TXT nella cartella 'data/' o configurare correttamente lo scraper.",
                metadata={"source": "Massimo AI placeholder"},
            )
        )

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=80)
    chunks = splitter.split_documents(docs)

    index_path_obj = Path(VECTOR_INDEX_PATH)
    index_dir = index_path_obj if index_path_obj.is_dir() else index_path_obj.parent
    index_dir.mkdir(parents=True, exist_ok=True)

    if (index_dir / "index.faiss").exists():
        vs = FAISS.load_local(str(index_dir), embeddings, allow_dangerous_deserialization=True)
        # Only add new/updated chunks to avoid reprocessing everything
        existing_urls = {doc.metadata.get("source") for doc in vs.docstore._dict.values() if doc.metadata.get("source")}
        new_chunks = [chunk for chunk in chunks if chunk.metadata.get("source") not in existing_urls]
        if new_chunks:
            vs.add_documents(new_chunks)
            log.info("FAISS index updated with %s new chunks (total docs: %s)", len(new_chunks), len(vs.index_to_docstore_id))
        else:
            log.info("FAISS index is up-to-date. No new chunks to add.")
    else:
        vs = FAISS.from_documents(chunks, embeddings)
        log.info("FAISS index created (%s chunks)", len(chunks))
    vs.save_local(str(index_dir))
    log.info(f"✅ Indexing completed: {len(docs)} total documents, {len(chunks)} chunks.")
    
    # Esporta i prodotti in CSV e Excel dopo l'indicizzazione
    export_products_to_csv_and_excel(os.path.join(index_dir.parent, "products_export.csv"), os.path.join(index_dir.parent, "products_export.xlsx"))

    return vs


vector_store = build_vector_store()

# ---------------------------------------------------------------------------
# Prompt setup (no chat_history placeholder – handled by memory)
# ---------------------------------------------------------------------------

# SYSTEM_PROMPT viene ora costruito dinamicamente in get_openai_response
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ---------------------------------------------------------------------------
# QA function (manual retrieval + llm)
# ---------------------------------------------------------------------------

def expand_query(q: str) -> str:
    """Espande la query dell'utente con sinonimi per migliorare la ricerca."""
    synonyms = {
        "pelle macchiata": "iperpigmentazione discromie antimacchia macchie scure",
        "profumi": "fragranze eau de parfum eau de toilette essenze",
        "crema viso": "skincare crema viso trattamento facciale siero",
        "shampoo": "detergente capelli lavaggio capelli",
        "balsamo": "conditioner capelli morbidi",
        "chi sei": "identità funzione ruolo assistente virtuale",
        "cosa sai fare": "capacità funzionalità compiti",
        "piano marketing": "piano compensi multilevel marketing unilevel guadagni",
        "prodotti per la casa": "detergenti casa pulizia ambiente",
        "integratori": "integrazione vitaminici nutrizionali",
        "trucco": "make up cosmetici",
        "promozioni": "offerta sconto",
    }
    for k, syn in synonyms.items():
        if k in q.lower():
            q += " " + syn
    return q


def get_openai_response(question: str) -> str:
    save_message("user", question)
    expanded = expand_query(question)

    try:
        docs = vector_store.similarity_search(expanded, k=7)
        log.debug(f"Documents retrieved before Python filter (names/titles): {[d.metadata.get('name', 'N/D') for d in docs]}")

        area_target = None
        if any(w in question.lower() for w in ("pelle", "viso", "macchiata", "cutanea")):
            area_target = {"face", "body"}
        elif any(w in question.lower() for w in ("capelli", "capillare")):
            area_target = {"hair"}
        elif any(w in question.lower() for w in ("profumi", "fragranze", "olfattivi")):
            area_target = {"perfume"}
        elif any(w in question.lower() for w in ("casa", "detergenza")):
            area_target = {"home"}
        elif any(w in question.lower() for w in ("integratori", "integrazione")):
            area_target = {"supplements"}
        elif any(w in question.lower() for w in ("trucco", "make up")):
            area_target = {"makeup"}
        elif any(w in question.lower() for w in ("promozioni", "offerta", "sconto")):
            area_target = {"promotions"}


        docs_for_context = docs
        if area_target:
            filtered_docs = [d for d in docs if d.metadata.get("application_area") in area_target]
            if not filtered_docs:
                log.warning(f"Python filter for application_area '{area_target}' removed all documents. LLM will rely on prompt and memory without specific product context.")
                docs_for_context = []
            else:
                docs_for_context = filtered_docs
                log.debug(f"Documents FILTERED in Python for application area ({area_target}): {[d.metadata.get('name', 'N/D') for d in docs_for_context]}")
        else:
            log.debug("No Python filter for application area applied.")

        context = "\n---\n".join(d.page_content for d in docs_for_context)
        
        chat_history_messages = memory.load_memory_variables({})["chat_history"]
        formatted_chat_history = "\n".join([f"{msg.type}: {msg.content}" for msg in chat_history_messages])
        
        full_system_prompt = (
            "Sei Massimo AI, assistente esperto dei prodotti e del piano marketing di Live On Plus. "
            "Rispondi solo con le informazioni presenti nel contesto e nella cronologia della chat. "
            "Sii conciso e diretto, ma esaustivo. "
            "Quando raccomandi un prodotto per un problema specifico (es. 'pelle macchiata'), è CRUCIALE che tu consideri la sua 'Area di Applicazione' e i suoi 'Concerns'. "
            "Se un prodotto sembra pertinente ma la sua 'Area di Applicazione' non corrisponde alla parte del corpo richiesta (es. un prodotto per capelli per un problema della pelle), DEVI: "
            "1. Indicare la categoria e l'area di applicazione CORRETTA del prodotto. "
            "2. Spiegare chiaramente perché il prodotto NON È ADATTO alla parte del corpo richiesta. "
            "3. EVITARE di consigliare il prodotto per un uso improprio. "
            "Se non trovi informazioni pertinenti o se la tua risposta si baserebbe su un'inferenza NON SUPPORTATA dal testo, dichiara chiaramente che non hai informazioni specifiche e OFFRI DI ESPLORARE LA CATEGORIA GENERALE più vicina. "
            "NON inventare informazioni (prezzi, link, descrizioni o usi). "
            f"Cronologia Chat:\n{formatted_chat_history}\n"
            f"Context:\n{context}"
        )

        messages = [
            SystemMessagePromptTemplate.from_template(full_system_prompt).format(),
            HumanMessagePromptTemplate.from_template("{question}").format(question=question)
        ]
        
        reply_content = llm.invoke(messages).content
        reply = reply_content.strip() if reply_content else ""
        log.debug(f"RAW response generated by LLM (before fallback): '{reply.strip()}'")

        memory.save_context({"input": question}, {"output": reply})

    except Exception as e:
        log.error(f"Errore nella generazione della risposta AI: {e}", exc_info=True)
        return "Si è verificato un errore tecnico interno. Non riesco a elaborare la tua richiesta al momento. Riprova più tardi."

    triggers = [
        "non ho informazioni", "non trovo", "non posso", 
        "non ho dati sufficienti", "non riesco a trovare informazioni specifiche",
        "non sono in grado di fornire informazioni specifiche"
    ]
    if any(t in reply.lower() for t in triggers) or not reply.strip():
        if "pelle macchiata" in question.lower():
            reply = (
                "Al momento non ho un prodotto specifico indicizzato per le macchie cutanee. Potresti valutare un "
                "consulto dermatologico o guardare sieri alla vitamina C / creme con SPF alto che spesso "
                "aiutano a uniformare l'incarnato."
            )
        elif "capelli" in question.lower():
            reply = (
                "Mi dispiace, non ho trovato una corrispondenza esatta per i prodotti per capelli che cerchi. "
                "Posso suggerirti di esplorare la categoria generale 'Cura Capelli' o altre sezioni?"
            )
        elif "piano marketing" in question.lower():
             reply = (
                "Il Piano Marketing di Live On Plus si basa sul Multilevel Marketing e sull'Unilevel, "
                "con diversi livelli di carriera (Customer, Junior, Visor, Super Visor, Ambassador) "
                "che offrono bonus in base a punti e struttura di rete. "
                "Per dettagli molto specifici (es. calcolo esatto dei bonus per ogni livello o la regola 60/40), "
                "potrebbe essere necessario consultare la documentazione ufficiale di Live On Plus, "
                "che al momento non ho completamente indicizzato per tutti i dettagli numerici. "
                "Posso provare a darti informazioni più generiche su come si guadagna, se ti interessa?"
            )
        elif any(kw in question.lower() for kw in ["chi sei", "cosa sai fare", "sei", "cosa fai", "chi sei tu", "presentati"]):
             reply = (
                 "Sono Massimo AI, il tuo assistente virtuale specializzato nei prodotti e nel piano marketing di Live On Plus. "
                 "Posso fornirti informazioni dettagliate sui nostri prodotti cosmetici (per viso, corpo, capelli, profumi), "
                 "sui prodotti per la casa e sugli integratori, oltre a spiegarti come funziona il nostro piano marketing. "
                 "Chiedimi pure!"
             )
        else:
            reply = (
                "Mi dispiace, la mia base conoscitiva al momento non contiene dettagli utili per questa "
                "richiesta. Vuoi che cerchi in un'altra categoria o che aggiorni il catalogo?"
            )

    save_message("assistant", reply)
    return reply


# ---------------------------------------------------------------------------
# CLI quick‑test (main execution logic)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    log.info("Massimo AI pronto! (ESC per uscire)")
    try:
        # La build_vector_store() viene chiamata all'import del modulo e gestisce lo scraping
        # Non è necessario chiamarla esplicitamente qui, a meno che non si voglia forzare un re-build.
        # Per un avvio pulito e re-scraping: cancella faiss_index/index.* e massimo.db, poi avvia main.py

        while True:
            q = input("\n> ")
            if q.strip().upper() == "ESC":
                break
            if not q.strip():
                continue
            print(get_openai_response(q))
    finally:
        # Il main_driver viene chiuso automaticamente da atexit
        pass # Nessuna azione qui per non chiudere il driver troppo presto
