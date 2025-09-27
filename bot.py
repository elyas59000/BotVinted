import requests
import time
import os

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

def check_vinted():
    url = "https://www.vinted.fr/api/v2/catalog/items"
    params = {
        "search_text": "nike running veste",
        "price_to": 40,
        "currency": "EUR",
        "order": "newest_first"
    }

    r = requests.get(url, params=params)
    data = r.json()

    for item in data.get("items", []):
        message = f"**{item['title']}** - {item['price']}€\n{item['url']}"
        requests.post(WEBHOOK_URL, json={"content": message})

if __name__ == "__main__":
    while True:
        check_vinted()
        time.sleep(300)  # vérifie toutes les 5 minutes
