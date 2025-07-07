import os
import time
import json
import csv
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler

# === Config ===
load_dotenv()
USER = os.getenv("LIVEONPLUS_USER")
PWD = os.getenv("LIVEONPLUS_PASSWORD")
BASE_URL = "https://liveonplus.it/"
OUTPUT_DIR = "data/scraper_all/"
SCREEN_DIR = os.path.join(OUTPUT_DIR, "screenshots")
PDF_DIR = os.path.join(OUTPUT_DIR, "pdf")
MAX_DEPTH = 4

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SCREEN_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

# === Utility ===
def get_driver():
    svc = Service(executable_path="chromedriver.exe")
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=svc, options=opts)

def login(driver):
    login_url = "https://liveonplus.it/index.php?route=account/login"
    driver.get(login_url)
    time.sleep(2)
    driver.save_screenshot("DEBUG_LOGIN_1.png")  # Prima di qualsiasi interazione
    print("[DEBUG] Screenshot login 1 salvato.")
    try:
        cookie_btn = driver.find_element(By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'accetta') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'accept')]")
        cookie_btn.click()
        time.sleep(1)
    except Exception:
        pass
    try:
        driver.find_element(By.NAME, "email").send_keys(USER)
        driver.find_element(By.NAME, "password").send_keys(PWD)
        driver.find_element(By.XPATH, "//input[@type='submit' or @value='Login']").click()
        print(f">>> Tentato login come {USER}")
        time.sleep(3)
        driver.save_screenshot("DEBUG_LOGIN_2.png")  # Dopo il click login
        print("[DEBUG] Screenshot login 2 salvato.")
        # Verifica login
        if "logout" in driver.page_source.lower() or "esci" in driver.page_source.lower():
            print("[INFO] Login riuscito!")
        elif "login" in driver.page_source.lower() or "accedi" in driver.page_source.lower():
            print("[ERRORE] Login NON riuscito! Verifica credenziali o presenza CAPTCHA.")
        else:
            print("[ATTENZIONE] Non riesco a determinare con certezza se il login è riuscito. Controlla gli screenshot.")
    except Exception as e:
        print(f"[ERRORE durante login]: {e}")

def is_internal(url):
    return url.startswith(BASE_URL) or url.startswith("/")

def safe_filename(url, base_url=BASE_URL):
    url_slug = url.replace(base_url, "")
    url_slug = re.sub(r'[<>:"/\\|?*&= ]', '_', url_slug)
    if not url_slug or url_slug == "_":
        url_slug = "home"
    return url_slug[:100]

def save_content(url, html, meta):
    url_slug = safe_filename(url)
    with open(f"{OUTPUT_DIR}/{url_slug}.json", "w", encoding="utf-8") as f:
        json.dump({"url": url, "meta": meta, "html": html}, f, ensure_ascii=False, indent=2)

def download_pdf(pdf_url):
    pdf_name = os.path.basename(pdf_url.split("?")[0])
    pdf_path = os.path.join(PDF_DIR, pdf_name)
    try:
        r = requests.get(pdf_url, timeout=10)
        if r.ok:
            with open(pdf_path, "wb") as f:
                f.write(r.content)
            return pdf_path
    except Exception:
        pass
    return ""

def save_screenshot(driver, url):
    name = safe_filename(url)
    img_path = os.path.join(SCREEN_DIR, f"{name}.png")
    try:
        driver.save_screenshot(img_path)
    except Exception:
        pass
    return img_path

def wait_for_products(driver, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-thumb, .product-layout, .product-grid, .tt-product, .product-list, li.product-item"))
        )
    except Exception as e:
        print("[AVVISO] Timeout caricamento prodotti:", e)

def safe_get(driver, url, retries=3):
    for i in range(retries):
        try:
            driver.get(url)
            wait_for_products(driver)
            return driver.page_source
        except Exception as e:
            print(f"[RETRY {i+1}] su {url}: {e}")
            time.sleep(2 * (i+1))
    raise Exception(f"Impossibile caricare {url} dopo {retries} tentativi")

# === Scraping prodotti multipli layout ===
def extract_products(soup, url, driver):
    prodotti = []
    selectors = [
        "div.product-thumb",
        "div.product-layout",
        "div.product-grid > div",
        "div.tt-product",
        "li.product-item"
    ]
    found = False
    for selector in selectors:
        for prod in soup.select(selector):
            found = True
            try:
                nome = ""
                link = ""
                img = ""
                prezzo = ""
                prezzo_scontato = ""
                sconto = ""
                descrizione = ""
                categoria = ""
                punti = ""
                pdf_links = []
                # Nome e link
                a = prod.find("a")
                if a:
                    nome = a.get("title") or a.text.strip()
                    link = urljoin(url, a.get("href"))
                # Immagine
                img_tag = prod.find("img")
                if img_tag:
                    img = urljoin(url, img_tag.get("src"))
                # Prezzi e sconti
                price_div = prod.find("p", class_="price")
                if price_div:
                    prezzo = price_div.text.strip()
                    special = price_div.find("span", class_="price-new")
                    if special:
                        prezzo_scontato = special.text.strip()
                    old = price_div.find("span", class_="price-old")
                    if old:
                        prezzo = old.text.strip()
                prodotto_info = {"nome": nome, "link": link, "url_origine": url, "immagine": img, "prezzo": prezzo,
                                "prezzo_scontato": prezzo_scontato, "sconto": sconto, "descrizione": "", "categoria": "",
                                "punti": "", "pdf": [], "screenshot": ""}
                if link:
                    try:
                        dettaglio_html = safe_get(driver, link)
                        dettaglio_soup = BeautifulSoup(dettaglio_html, "html.parser")
                        desc_div = dettaglio_soup.find("div", id="tab-description")
                        if desc_div:
                            prodotto_info["descrizione"] = desc_div.get_text(separator="\n", strip=True)
                        bc = dettaglio_soup.find("ul", class_="breadcrumb")
                        if bc:
                            cat = [li.text.strip() for li in bc.find_all("li")]
                            prodotto_info["categoria"] = " > ".join(cat)
                        punti = dettaglio_soup.find("span", class_="reward-points")
                        if punti:
                            prodotto_info["punti"] = punti.text.strip()
                        pdfs = [urljoin(link, a["href"]) for a in dettaglio_soup.find_all("a") if a.get("href", "").endswith(".pdf")]
                        prodotto_info["pdf"] = []
                        for pdf_url in pdfs:
                            pdf_path = download_pdf(pdf_url)
                            if pdf_path:
                                prodotto_info["pdf"].append(pdf_path)
                        prodotto_info["screenshot"] = save_screenshot(driver, link)
                    except Exception as e:
                        print("[ERRORE Dettaglio prodotto]:", e)
                prodotti.append(prodotto_info)
            except Exception as e:
                print("[ERRORE Prodotto]:", e)
                continue
    if not found:
        print("[DEBUG] Nessun prodotto trovato su", url)
    return prodotti

def extract_pdfs_and_cataloghi(soup, url):
    pdfs = []
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if href.endswith(".pdf"):
            pdf_url = urljoin(url, href)
            pdf_path = download_pdf(pdf_url)
            if pdf_path:
                pdfs.append({"pdf_url": pdf_url, "pdf_path": pdf_path, "pagina": url})
    return pdfs

def crawl_url(driver, url, crawled_urls=None, depth=0, prodotti=None, pdfs=None):
    if crawled_urls is None:
        crawled_urls = set()
    if prodotti is None:
        prodotti = []
    if pdfs is None:
        pdfs = []
    url = url.split("#")[0]  # Ignora ancore
    if url in crawled_urls or depth > MAX_DEPTH or not is_internal(url):
        return prodotti, pdfs
    print(f"[INFO] Visito: {url}")
    try:
        page_source = safe_get(driver, url)
        save_screenshot(driver, url)
        soup = BeautifulSoup(page_source, "html.parser")
        prodotti_in_pagina = extract_products(soup, url, driver)
        if prodotti_in_pagina:
            prodotti.extend(prodotti_in_pagina)
        pdfs_in_pagina = extract_pdfs_and_cataloghi(soup, url)
        if pdfs_in_pagina:
            pdfs.extend(pdfs_in_pagina)
        save_content(url, page_source, {"prodotti": len(prodotti_in_pagina), "pdfs": len(pdfs_in_pagina)})
        crawled_urls.add(url)
        # Paginazione
        next_link = soup.find("a", string=re.compile("Successivo|Next|>|»"))
        if next_link and next_link.get("href"):
            full_link = urljoin(url, next_link["href"])
            if is_internal(full_link) and full_link not in crawled_urls:
                crawl_url(driver, full_link, crawled_urls, depth, prodotti, pdfs)
        # Altri link interni
        for a in soup.find_all("a"):
            link = a.get("href")
            if link:
                full_link = urljoin(url, link)
                if is_internal(full_link) and full_link not in crawled_urls:
                    crawl_url(driver, full_link, crawled_urls, depth+1, prodotti, pdfs)
    except Exception as e:
        print(f"[ERRORE su {url}]: {e}")
    return prodotti, pdfs

def save_prodotti(prodotti):
    with open(os.path.join(OUTPUT_DIR, "prodotti.json"), "w", encoding="utf-8") as f:
        json.dump(prodotti, f, ensure_ascii=False, indent=2)
    keys = list(prodotti[0].keys()) if prodotti else []
    with open(os.path.join(OUTPUT_DIR, "prodotti.csv"), "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for p in prodotti:
            writer.writerow(p)
    with open(os.path.join(OUTPUT_DIR, "prodotti.txt"), "w", encoding="utf-8") as f:
        for i, p in enumerate(prodotti):
            f.write(f"PRODOTTO {i+1}\n")
            for k, v in p.items():
                f.write(f"{k}: {v}\n")
            f.write("-"*50 + "\n")

def save_pdfs(pdfs):
    with open(os.path.join(OUTPUT_DIR, "tutti_pdf.json"), "w", encoding="utf-8") as f:
        json.dump(pdfs, f, ensure_ascii=False, indent=2)

def scheduled_scrape():
    print(f"\n[INFO] Avvio scraping: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    driver = get_driver()
    try:
        login(driver)
        prodotti, pdfs = crawl_url(driver, BASE_URL)
        save_prodotti(prodotti)
        save_pdfs(pdfs)
        print(f"[INFO] Scraping completato! {len(prodotti)} prodotti, {len(pdfs)} PDF trovati.")
    except Exception as e:
        print(f"[ERRORE] Durante scraping: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_scrape, 'interval', hours=1)
    print("SCRAPER ULTRA AVVIATO. OGNI ORA ESTRAPOLA TUTTO!\nCtrl+C per fermare.")
    try:
        scheduled_scrape()  # Primo scraping subito
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scraper fermato manualmente.")
