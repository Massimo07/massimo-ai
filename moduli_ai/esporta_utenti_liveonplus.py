import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import re

# === CARICA CREDENZIALI ===
load_dotenv()
USERNAME = os.getenv("LIVEONPLUS_USERNAME")
PASSWORD = os.getenv("LIVEONPLUS_PASSWORD")

# === PERCORSO DRIVER ===
PATH_CHROMEDRIVER = "chromedriver.exe"

def get_country_from_phone(phone):
    prefix_map = {
        "+39": "Italia",
        "+40": "Romania",
        "+34": "Spagna",
        "+33": "Francia",
        "+49": "Germania",
        "+351": "Portogallo",
        "+41": "Svizzera",
        "+44": "UK",
        "+30": "Grecia",
        "+32": "Belgio",
        "+420": "Repubblica Ceca",
        "+421": "Slovacchia",
        "+48": "Polonia",
        "+43": "Austria",
        "+36": "Ungheria",
        "+380": "Ucraina",
        "+372": "Estonia",
        "+370": "Lituania",
        "+371": "Lettonia",
        "+7": "Russia/Kazakhstan",
        "+386": "Slovenia"
    }
    for k in prefix_map:
        if phone.startswith(k):
            return prefix_map[k]
    return "Altro"

def get_age_range(age_str):
    try:
        age = int(age_str)
        if age < 18:
            return "<18"
        elif 18 <= age <= 25:
            return "18-25"
        elif 26 <= age <= 50:
            return "26-50"
        else:
            return "50+"
    except:
        return ""

def main():
    # === AVVIO BROWSER ===
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    # === LOGIN ===
    driver.get("https://user.liveonplus.it/login")
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "fname"))).send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # === ATTESA DASHBOARD ===
    WebDriverWait(driver, 15).until(EC.url_contains("dashboard"))

    # === VAI SU TREE-VIEW ===
    driver.get("https://user.liveonplus.it/tree-view")
    time.sleep(3)

    utenti = []
    while True:
        rows = driver.find_elements(By.CSS_SELECTOR, ".MuiTableRow-root")
        for row in rows:
            cols = row.find_elements(By.CSS_SELECTOR, ".MuiTableCell-root")
            if len(cols) >= 3:
                codice = cols[0].text.strip()
                nome_cognome = cols[1].text.strip().split()
                nome = nome_cognome[0] if nome_cognome else ""
                cognome = " ".join(nome_cognome[1:]) if len(nome_cognome) > 1 else ""
                livello = cols[2].text.strip()
                # click "i" per dettagli (cell, provincia, sesso, età)
                try:
                    info_btn = row.find_element(By.CSS_SELECTOR, "button[title='Dettagli']")
                    driver.execute_script("arguments[0].click();", info_btn)
                    time.sleep(1)
                    modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiDialog-root")))
                    fields = modal.text
                    cell = re.search(r"Cellulare:\s*([+\d\s]+)", fields)
                    cell = cell.group(1).replace(" ", "") if cell else ""
                    provincia = re.search(r"Provincia:\s*(\w+)", fields)
                    provincia = provincia.group(1) if provincia else ""
                    sesso = re.search(r"Sesso:\s*(\w+)", fields)
                    sesso = sesso.group(1) if sesso else ""
                    eta = re.search(r"Età:\s*(\d+)", fields)
                    eta = eta.group(1) if eta else ""
                    stato = get_country_from_phone(cell)
                    eta_range = get_age_range(eta)
                    utenti.append({
                        "Codice": codice,
                        "Nome": nome,
                        "Cognome": cognome,
                        "Cellulare": cell,
                        "Sesso": sesso,
                        "Provincia": provincia,
                        "Età": eta,
                        "Fascia Età": eta_range,
                        "Stato": stato
                    })
                    # chiudi modale
                    close_btn = modal.find_element(By.CSS_SELECTOR, "button[aria-label='close']")
                    driver.execute_script("arguments[0].click();", close_btn)
                    time.sleep(0.3)
                except Exception as e:
                    pass
        # PAGINAZIONE
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Go to next page']")
            if next_btn.is_enabled():
                driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(2)
            else:
                break
        except:
            break

    # === ESPORTA EXCEL ===
    df = pd.DataFrame(utenti)
    df.to_excel("utenti_liveonplus.xlsx", index=False)
    print("✅ Esportazione completata! File: utenti_liveonplus.xlsx")
    driver.quit()

if __name__ == "__main__":
    main()
