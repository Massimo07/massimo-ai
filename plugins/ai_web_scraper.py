# /plugins_ai/ai_web_scraper.py

import requests
from bs4 import BeautifulSoup
import openai

class AIWebScraper:
    def __init__(self, api_key):
        openai.api_key = api_key

    def scrape_and_summarize(self, url, language="it"):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.get_text()
        prompt = (
            f"Riassumi il contenuto di questa pagina web:\n{text[:6000]}\nLingua output: {language}."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# scraper = AIWebScraper(api_key="TUA_OPENAI_KEY")
# summary = scraper.scrape_and_summarize("https://www.openai.com/")
