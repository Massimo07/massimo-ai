import os
import csv
import json
import time
import traceback
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIGURAZIONE ---
LOGIN_URL = "https://liveonplus.it/index.php?route=account/login"
BASE_URL = "https://liveonplus.it/"
USER = "maxmarfisi@gmail.com"
PWD = "Ma551m07."
ROOT = Path(__file__).parent

CSV_PATH = ROOT / "massimoai_products_full.csv"
JSON_PATH = ROOT / "massimoai_products_full.json"
IMG_DIR = ROOT / "images"
PDF_DIR = ROOT / "schede_prodotti_pdf"
LOG_PATH = ROOT / "scraper_errori.log"

for d in [IMG_DIR, PDF_DIR]:
    d.mkdir(exist_ok=True)

def get_driver():
    svc = Service(executable_path="chromedriver.exe")
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=svc, options=opts)

def login(driver):
    driver.get(LOGIN_URL)
    time.sleep(2)
    # Gestione banner cookie
    try:
        cookie_btn = driver.find_element(By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'accetta') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'accept')]")
        cookie_btn.click()
        print("Banner cookie accettato.")
        time.sleep(1)
    except Exception:
        pass

    # Ricerca campo EMAIL
    try:
        email_input = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
    except Exception:
        try:
            email_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "input-email"))
            )
        except Exception:
            email_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'email') or contains(@placeholder, 'Email')]"))
            )

    # Ricerca campo PASSWORD
    try:
        password_input = driver.find_element(By.NAME, "password")
    except Exception:
        try:
            password_input = driver.find_element(By.ID, "input-password")
        except Exception:
            password_input = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'ordine') or contains(@placeholder, 'Password')]")

    email_input.clear()
    email_input.send_keys(USER)
    password_input.clear()
    password_input.send_keys(PWD)

    # Pulsante login
    try:
        driver.find_element(By.XPATH, "//button[contains(translate(., 'ACCESSO', 'accesso'), 'accesso') or contains(., 'Accedi') or contains(., 'Login')]").click()
    except Exception:
        try:
            driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        except Exception:
            raise Exception("Pulsante login non trovato!")

    time.sleep(3)
    print("Login completato.")

def get_all_category_links(driver, url, visited=None, depth=0, max_depth=3):
    """Ricorsione limitata per evitare cicli infiniti sulle categorie."""
    if visited is None:
        visited = set()
    if depth > max_depth:
        return set()
    try:
        driver.get(url)
        time.sleep(1.2)
    except Exception as e:
        print(f"Errore su {url}: {e}")
        return set()
    category_links = set()
    for a in driver.find_elements(By.CSS_SELECTOR, "a[href*='path=']"):
        href = a.get_attribute("href")
        if href and "product_id" not in href and href not in visited:
            category_links.add(href)
    for subcat in category_links.copy():
        if subcat not in visited:
            visited.add(subcat)
            deeper = get_all_category_links(driver, subcat, visited, depth + 1, max_depth)
            category_links.update(deeper)
    return category_links

def download_file(url, save_dir, default_name):
    import requests
    try:
        fname = url.split("/")[-1]
        if not fname or "." not in fname:
            fname = default_name
        out_path = save_dir / fname
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            with open(out_path, "wb") as f:
                f.write(r.content)
            return str(out_path)
    except Exception:
        pass
    return ""

def get_product_details(driver, url):
    details = {"url": url, "error": ""}
    try:
        driver.get(url)
        time.sleep(1.8)
        details["name"] = driver.find_element(By.CSS_SELECTOR, "h1, h2.tt-title").text.strip()
        details["price"] = driver.find_element(By.CSS_SELECTOR, ".price, .tt-price").text.strip()
        details["category"] = " > ".join([x.text.strip() for x in driver.find_elements(By.CSS_SELECTOR, ".breadcrumb a")])
        desc = ""
        try:
            desc = driver.find_element(By.CSS_SELECTOR, "#product-description, .product-description, .desc").text.strip()
        except Exception:
            pass
        details["description"] = desc
        # Immagini
        images = []
        for img in driver.find_elements(By.CSS_SELECTOR, ".product-info img, .product-image img, img"):
            src = img.get_attribute("src")
            if src and "logo" not in src and src not in images:
                images.append(src)
        details["image_urls"] = images
        if images:
            img_paths = []
            for idx, img_url in enumerate(images):
                img_name = f"{details['name'][:30].replace(' ','_')}_{idx}.jpg"
                path = download_file(img_url, IMG_DIR, img_name)
                if path:
                    img_paths.append(path)
            details["downloaded_images"] = img_paths
        # PDF
        pdfs = []
        for a in driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf']"):
            href = a.get_attribute("href")
            if href and href not in pdfs:
                pdfs.append(href)
        details["pdf_links"] = pdfs
        if pdfs:
            pdf_paths = []
            for idx, pdf_url in enumerate(pdfs):
                pdf_name = f"{details['name'][:30].replace(' ','_')}_{idx}.pdf"
                path = download_file(pdf_url, PDF_DIR, pdf_name)
                if path:
                    pdf_paths.append(path)
            details["downloaded_pdfs"] = pdf_paths
        # Codice prodotto
        try:
            details["code"] = driver.find_element(By.CSS_SELECTOR, ".product-code, #product-code").text.strip()
        except Exception:
            details["code"] = ""
        # INCI (ingredienti)
        try:
            details["inci"] = driver.find_element(By.XPATH, "//strong[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'inci')]/following-sibling::span").text.strip()
        except Exception:
            details["inci"] = ""
        details["last_updated"] = datetime.utcnow().isoformat()
    except Exception as e:
        details["error"] = str(e) + "\n" + traceback.format_exc()
    return details

def main():
    driver = get_driver()
    login(driver)
    print("\nRicerca di tutte le categorie e sottocategorie...")
    all_categories = get_all_category_links(driver, BASE_URL, max_depth=3)
    print(f"\nTrovate {len(all_categories)} categorie/sottocategorie TOT.")
    all_products = set()
    for cat in sorted(all_categories):
        print(f"\n---\nCategoria: {cat}")
        try:
            driver.get(cat)
            time.sleep(1.2)
            prods = set([a.get_attribute("href") for a in driver.find_elements(By.CSS_SELECTOR, "a[href*='product/product']") if a.get_attribute("href")])
            print(f"Categoria: {cat} – {len(prods)} prodotti")
            all_products.update(prods)
        except Exception as e:
            print(f"Errore sulla categoria {cat}: {e}")
    print(f"\n=== TOTALE UNICO PRODOTTI TROVATI: {len(all_products)} ===")
    # Scrape dettagli
    all_data = []
    with open(LOG_PATH, "w", encoding="utf-8") as elog:
        for i, url in enumerate(sorted(all_products), 1):
            print(f"[{i}/{len(all_products)}] {url}")
            data = get_product_details(driver, url)
            all_data.append(data)
            if data.get("error"):
                elog.write(f"{url}\n{data['error']}\n\n")
            time.sleep(0.7)
    # Salva tutto
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        fieldnames = sorted({k for d in all_data for k in d.keys()})
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_data:
            writer.writerow(row)
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    print(f"\nTutti i dati sono stati salvati in {CSV_PATH} e {JSON_PATH}!")
    driver.quit()

if __name__ == "__main__":
    main()
