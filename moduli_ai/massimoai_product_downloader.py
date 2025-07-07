import time
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# --- CONFIGURAZIONI ---
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

def parse_product(driver, url):
    driver.get(url)
    time.sleep(1.5)
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
    # PDF (primo link .pdf nella pagina)
    try:
        pdf_link = driver.find_element(By.XPATH, "//a[contains(@href,'.pdf')]").get_attribute("href")
        pdf_name = os.path.basename(pdf_link).split("?")[0]
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        # Scarica il PDF
        import requests
        r = requests.get(pdf_link)
        if r.ok:
            with open(pdf_path, "wb") as f:
                f.write(r.content)
            print(f"Scaricato PDF: {pdf_name}")
            data["pdf"] = pdf_name
        else:
            data["pdf"] = ""
    except:
        data["pdf"] = ""
    return data

if __name__ == "__main__":
    # Carica tutti i link prodotti
    with open("all_product_links.txt", "r", encoding="utf-8") as f:
        links = [x.strip() for x in f if x.strip()]
    driver = get_driver()
    login(driver)
    all_data = []
    for idx, url in enumerate(links):
        print(f"Scarico prodotto {idx+1}/{len(links)}: {url}")
        try:
            prod = parse_product(driver, url)
            all_data.append(prod)
        except Exception as e:
            print(f"Errore {url}: {e}")
    driver.quit()
    # Salva CSV
    with open("prodotti_completi.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["url", "name", "price", "desc", "image", "pdf"])
        writer.writeheader()
        for d in all_data:
            writer.writerow(d)
    print("\nFINITO! Trovi tutto in prodotti_completi.csv e i PDF in /pdf\n")
