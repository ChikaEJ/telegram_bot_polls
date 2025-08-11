import os

import requests

TG_API_KEY = os.getenv("TELEGRAM_BOT_TOKEN")
webhook = os.getenv("NGROK_TUNNEL_URL")

response = requests.get(
    f"https://api.telegram.org/bot{TG_API_KEY}/setWebhook?url={webhook}"
)
print(response.json())

