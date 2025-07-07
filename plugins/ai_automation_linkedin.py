# /plugins_ai/ai_automation_linkedin.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AILinkedInAutomation:
    def __init__(self, email, password, browser="chrome"):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome() if browser == "chrome" else webdriver.Firefox()

    def login(self):
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys(self.email)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def send_message(self, profile_url, message):
        self.driver.get(profile_url)
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "message-anywhere-button").click()
        time.sleep(1)
        textarea = self.driver.find_element(By.TAG_NAME, "textarea")
        textarea.send_keys(message)
        textarea.send_keys(Keys.ENTER)
        time.sleep(1)

    def quit(self):
        self.driver.quit()

# USO:
# bot = AILinkedInAutomation("tua_email", "tua_password")
# bot.login()
# bot.send_message("https://www.linkedin.com/in/target-profile", "Ciao! Vorrei connettermi con te.")
# bot.quit()
