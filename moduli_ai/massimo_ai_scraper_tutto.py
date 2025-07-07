import os
import time
import csv
import json
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

BASE_URL = "https://liveonplus.it/index.php?route=product/category&path=101"
DOWNLOAD_DIR = "prodotti_liveonplus"
CSV_PATH = os.path.join(DOWNLOAD_DIR, "prodotti.csv")
JSON_PATH = os.path.join(DOWNLOAD_DIR, "prodotti.json")
LOG_PATH = os.path.join(DOWNLOAD_DIR, "errori.log")
COOKIES_PATH = "cookies.json"  # <--- Questo file lo esporti da browser loggato!
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def start_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
    # chrome_options.add_argument("--headless=new")  # Attiva solo se vuoi non vedere la finestra
    return webdriver.Chrome(options=chrome_options)

def load_cookies(driver, cookies_path):
    with open(cookies_path, "r", encoding="utf-8") as f:
        cookies = json.load(f)
    for cookie in cookies:
        # Alcune estensioni mettono "sameSite": "unspecified"
        if "sameSite" in cookie and cookie["sameSite"].lower() == "unspecified":
            cookie["sameSite"] = "Strict"
        driver.add_cookie({k: v for k, v in cookie.items() if k in ["name", "value", "domain", "path", "expiry", "secure", "httpOnly", "sameSite"]})

def login_with_cookies(driver, base_url, cookies_path):
    driver.get(base_url)
    time.sleep(2)
    load_cookies(driver, cookies_path)
    driver.refresh()
    time.sleep(2)

def get_all_category_links(driver, url, visited=None):
    if visited is None:
        visited = set()
    driver.get(url)
    time.sleep(1.5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = []
    for a in soup.select("a[href*='category&path=']"):
        href = a.get("href")
        if href and href not in visited and "javascript" not in href:
            links.append(href)
    visited.add(url)
    all_cats = [url]
    for l in set(links):
        if l not in visited:
            all_cats.extend(get_all_category_links(driver, l, visited))
    return list(set(all_cats))

def get_all_product_links(driver, category_url):
    links = set()
    page = 1
    while True:
        url_paged = category_url
        if "&page=" not in category_url and page > 1:
            url_paged = category_url + f"&page={page}"
        elif "&page=" in category_url:
            url_paged = re.sub(r"&page=\d+", f"&page={page}", category_url)
        driver.get(url_paged)
        time.sleep(1.2)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for a in soup.select("a[href*='product/product']"):
            name = a.text.strip()
            href = a['href']
            if name and "product_id" in href:
                links.add((name, href))
        pagination = soup.select_one(".pagination")
        if pagination and str(page+1) in pagination.text:
            page += 1
        else:
            break
    return list(links)

def get_product_details(driver, url, category_folder):
    try:
        driver.get(url)
        time.sleep(1.5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        data = {}
        data["nome"] = soup.select_one("h1").text.strip() if soup.select_one("h1") else ""
        data["prezzo"] = soup.select_one(".price").text.strip() if soup.select_one(".price") else ""
        data["descrizione"] = soup.select_one("#tab-description").text.strip() if soup.select_one("#tab-description") else ""
        data["categorie_full"] = " > ".join([li.text.strip() for li in soup.select(".breadcrumb li a") if li.text.strip()])
        data["url"] = url

        details_text = ""
        for tab in soup.find_all(["table", "ul", "dl", "div"], class_=re.compile("(tab|info|dettaglio|detail)", re.I)):
            details_text += tab.get_text(separator="\n", strip=True) + "\n"

        patterns = [
            ("ean", r"\bEAN[\s:]*([0-9A-Z]+)\b"),
            ("sku", r"\bSKU[\s:]*([0-9A-Z\-]+)\b"),
            ("codice_prodotto", r"\bCod(?:ice)?\s*([0-9A-Z\-]+)\b"),
            ("quantita", r"\bQuantità[\s:]*([0-9]+)\b"),
        ]
        for k, pat in patterns:
            m = re.search(pat, details_text, re.I)
            if m:
                data[k] = m.group(1)

        data["immagini"] = []
        for img in soup.select(".thumbnails img, .product-image img, .image img"):
            img_url = img.get("src") or img.get("data-src")
            if img_url:
                try:
                    img_data = requests.get(img_url).content
                    img_filename = os.path.join(category_folder, os.path.basename(img_url.split("?")[0]))
                    with open(img_filename, "wb") as f:
                        f.write(img_data)
                    data["immagini"].append(img_filename)
                except Exception as e:
                    data.setdefault("errori_img", []).append(f"{img_url}: {e}")

        data["allegati"] = []
        for a in soup.select("a[href$='.pdf'], a[href$='.doc'], a[href$='.docx']"):
            href = a.get("href", "")
            if href:
                try:
                    file_data = requests.get(href).content
                    file_name = os.path.join(category_folder, os.path.basename(href.split("?")[0]))
                    with open(file_name, "wb") as f:
                        f.write(file_data)
                    data["allegati"].append(file_name)
                except Exception as e:
                    data.setdefault("errori_allegati", []).append(f"{href}: {e}")

        data["ingredienti"] = ""
        inci_match = re.search(r"\bINCI[\s:]*([A-Za-z0-9 ,\-;]+)", details_text, re.I)
        if inci_match:
            data["ingredienti"] = inci_match.group(1)
        data["attributi"] = details_text
        data["varianti"] = ""
        varianti_match = re.findall(r"\b([0-9]+ ?ml|[0-9]+ ?g|colore: ?[A-Za-z]+)\b", details_text, re.I)
        if varianti_match:
            data["varianti"] = ", ".join(set(varianti_match))
        data["recensioni"] = ""
        rec_box = soup.find("div", id="tab-review")
        if rec_box:
            data["recensioni"] = rec_box.get_text(separator="\n", strip=True)
        data["html_raw_file"] = ""
        html_path = os.path.join(category_folder, f"{data['nome'][:50].replace(' ','_')}_raw.html")
        try:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(str(soup.prettify()))
            data["html_raw_file"] = html_path
        except Exception as e:
            data.setdefault("errori_html", []).append(str(e))
        return data
    except Exception as e:
        return {"url": url, "error": str(e)}

def main():
    driver = start_driver()
    # Login tramite cookie reale!
    login_with_cookies(driver, BASE_URL, COOKIES_PATH)
    print("Sessione autenticata. Inizio scraping definitivo.")
    all_categories = get_all_category_links(driver, BASE_URL)
    print(f"Trovate {len(all_categories)} categorie/sottocategorie totali.")
    all_products_links = set()
    for cat in sorted(all_categories):
        print(f"\n---\nCategoria: {cat}")
        prods = get_all_product_links(driver, cat)
        print(f"Categoria: {cat} – {len(prods)} prodotti")
        all_products_links.update(prods)
    print(f"\n=== TOTALE UNICO PRODOTTI TROVATI: {len(all_products_links)} ===")
    all_data = []
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as elog:
        for i, (prod_name, url) in enumerate(sorted(all_products_links), 1):
            cat_folder = os.path.join(DOWNLOAD_DIR, prod_name.replace(" ", "_")[:60])
            os.makedirs(cat_folder, exist_ok=True)
            print(f"[{i}/{len(all_products_links)}] {prod_name} - {url}")
            data = get_product_details(driver, url, cat_folder)
            data["nome"] = prod_name or data.get("nome", "")
            all_data.append(data)
            if data.get("error"):
                elog.write(f"{url}\n{data['error']}\n\n")
            time.sleep(0.6)
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
