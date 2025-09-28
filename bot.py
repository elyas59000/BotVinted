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

    if "items" not in data:
        print("⚠️ Erreur API Vinted :", data)
        return

    for item in data["items"]:
        message = f"**{item['title']}** - {item['price']}€\n{item['url']}"
        requests.post(WEBHOOK_URL, json={"content": message})

if __name__ == "__main__":
    # Si GitHub Actions est en train d’exécuter → une seule fois
    if os.getenv("GITHUB_ACTIONS") == "true":
        check_vinted()
    else:
        # Si tu lances en local → boucle infinie toutes les 5 min
        while True:
            check_vinted()
            time.sleep(300)
