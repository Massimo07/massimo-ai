import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

LOGIN_URL = "https://liveonplus.it/index.php?route=account/login"
USER = "maxmarfisi@gmail.com"
PWD = "Ma551m07."

def start_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")  # Disattiva headless per vedere la finestra!
    chrome_options.add_argument("--window-size=1200,900")
    return webdriver.Chrome(options=chrome_options)

def login_and_debug(driver):
    driver.get(LOGIN_URL)
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys(USER)
    driver.find_element(By.NAME, "password").send_keys(PWD)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    print("Login inviato, aspetto...")
    time.sleep(5)
    # Ora salva la pagina per vedere se sei loggato
    with open("debug_login.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(">>> Pagina post-login salvata come debug_login.html!")
    input("Guarda la finestra e premi INVIO per chiudere...")
    driver.quit()

if __name__ == "__main__":
    driver = start_driver()
    login_and_debug(driver)
