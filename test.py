import requests

# Remplace par ton URL de webhook Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/1421825987901128746/dtUO51oXO-lsWBDzmZSU-I0-dyDuLXhZRg3jiXNdSbGLezR15906Nu7xG6Edz6OmZEwE"

message = {"content": "✅ Test du webhook Discord depuis VSCode"}
r = requests.post(WEBHOOK_URL, json=message)

print("Code retour :", r.status_code)
print("Réponse :", r.text)
