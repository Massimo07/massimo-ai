import time
import os
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

USER = "maxmarfisi@gmail.com"
PWD = "Ma551m07."
LOGIN_URL = "https://liveonplus.it/index.php?route=account/login"
PDF_DIR = "pdf"
os.makedirs(PDF_DIR, exist_ok=True)

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
    try:
        cookie_btn = driver.find_element(By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'accetta') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'accept')]")
        cookie_btn.click()
        time.sleep(1)
        print("Banner cookie accettato/chiuso.")
    except Exception:
        print("Nessun banner cookie da chiudere (ok).")
    driver.find_element(By.NAME, "email").send_keys(USER)
    driver.find_element(By.NAME, "password").send_keys(PWD)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(3)
    print("Login completato.")

def get_all_category_links(driver, url, visited=None):
    if visited is None:
        visited = set()
    driver.get(url)
    time.sleep(1.2)
    category_links = set()
    for a in driver.find_elements(By.CSS_SELECTOR, "a[href*='path=']"):
        href = a.get_attribute("href")
        if href and "product_id" not in href and href not in visited:
            category_links.add(href)
    for subcat in category_links.copy():
        if subcat not in visited:
            visited.add(subcat)
            deeper = get_all_category_links(driver, subcat, visited)
            category_links.update(deeper)
    return category_links

def get_product_links_for_category(driver, category_url):
    product_links = set()
    page_url = category_url
    page_count = 1
    while True:
        driver.get(page_url)
        time.sleep(1.7)
        prods = [a.get_attribute("href") for a in driver.find_elements(By.CSS_SELECTOR, "a[href*='product/product']")]
        product_links.update([p for p in prods if p])
        next_buttons = driver.find_elements(By.CSS_SELECTOR, ".pagination .next a, .pagination li.next a")
        if next_buttons:
            page_url = next_buttons[0].get_attribute("href")
            page_count += 1
        else:
            break
    return product_links

def parse_product(driver, url):
    driver.get(url)
    time.sleep(1.3)
    data = {"url": url}
    try:
        data["name"] = driver.find_element(By.CSS_SELECTOR, "h1, h2.tt-title").text
    except:
        data["name"] = ""
    try:
        data["price"] = driver.find_element(By.CSS_SELECTOR, ".price, .tt-price").text
    except:
        data["price"] = ""
    try:
        data["desc"] = driver.find_element(By.CSS_SELECTOR, "#product-description, .product-description, .desc").text
    except:
        data["desc"] = ""
    try:
        data["image"] = driver.find_element(By.CSS_SELECTOR, ".product-info img, .product-image img, img").get_attribute("src")
    except:
        data["image"] = ""
    # PDF
    try:
        pdf_link = driver.find_element(By.XPATH, "//a[contains(@href,'.pdf')]").get_attribute("href")
        pdf_name = os.path.basename(pdf_link).split("?")[0]
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        if not os.path.exists(pdf_path):  # Scarica solo se non esiste già!
            r = requests.get(pdf_link)
            if r.ok:
                with open(pdf_path, "wb") as f:
                    f.write(r.content)
                print(f"Scaricato PDF: {pdf_name}")
        data["pdf"] = pdf_name
    except:
        data["pdf"] = ""
    return data

def update_products_csv(new_products, csv_file="prodotti_completi.csv"):
    # Aggiorna prodotti solo se nuovi o cambiati (in base a url)
    products_dict = {}
    if os.path.exists(csv_file):
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products_dict[row["url"]] = row
    for prod in new_products:
        # Aggiorna SOLO se dati diversi o nuovo
        old = products_dict.get(prod["url"], {})
        changed = any(prod[k] != old.get(k, "") for k in prod)
        if changed:
            products_dict[prod["url"]] = prod
    # Salva tutto
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["url", "name", "price", "desc", "image", "pdf"])
        writer.writeheader()
        for d in products_dict.values():
            writer.writerow(d)
    print(f"\nCSV AGGIORNATO: {csv_file} ({len(products_dict)} prodotti totali)")

def super_scraper_every_3h():
    while True:
        driver = get_driver()
        login(driver)
        all_categories = get_all_category_links(driver, "https://liveonplus.it/")
        all_products = set()
        for cat in sorted(all_categories):
            prods = get_product_links_for_category(driver, cat)
            all_products.update(prods)
        print(f"\nTrovati {len(all_products)} link prodotto.")
        all_data = []
        for idx, url in enumerate(all_products):
            print(f"Scarico prodotto {idx+1}/{len(all_products)}: {url}")
            try:
                prod = parse_product(driver, url)
                all_data.append(prod)
            except Exception as e:
                print(f"Errore {url}: {e}")
        driver.quit()
        update_products_csv(all_data)
        print("Attendo 3 ore per il prossimo ciclo...\n")
        time.sleep(3 * 60 * 60)  # 3 ore

if __name__ == "__main__":
    super_scraper_every_3h()
