import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Carica variabili d'ambiente
load_dotenv()
LIVEONPLUS_USER = os.getenv("LIVEONPLUS_USER")
LIVEONPLUS_PASSWORD = os.getenv("LIVEONPLUS_PASSWORD")
LOGIN_URL = os.getenv("LIVEONPLUS_LOGIN_URL", "https://user.liveonplus.it/")

def verifica_registrazione(codice_utente):
    # Configura Selenium headless (senza aprire finestra)
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(LOGIN_URL)
        time.sleep(2)
        
        # Login
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(LIVEONPLUS_USER)
        password_input.send_keys(LIVEONPLUS_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)

        # Vai nella genealogia (devi aggiustare l’URL se cambia)
        driver.get("https://user.liveonplus.it/genealogy") 
        time.sleep(3)

        # Cerca il codice utente nella pagina
        page_source = driver.page_source
        if codice_utente in page_source:
            print(f"✅ L’utente con codice {codice_utente} RISULTA registrato.")
            return True
        else:
            print(f"❌ L’utente con codice {codice_utente} NON risulta registrato.")
            return False

    except Exception as e:
        print(f"Errore durante la verifica: {e}")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    codice = input("Inserisci il codice utente da verificare: ")
    verifica_registrazione(codice)
