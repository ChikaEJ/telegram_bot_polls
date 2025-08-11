import os

import requests


TG_API_KEY = os.getenv("TELEGRAM_BOT_TOKEN")
webhook = os.getenv("NGROK_TUNNEL_URL")

response = requests.get(
    f"https://api.telegram.org/bot{TG_API_KEY}/setWebhook?url={webhook}"
)
print(response.json())

# url = f"https://api.telegram.org/bot8026699243:AAGkm08AgAQCz-7W9Dhw8yjZCeKVbtg04RY/deleteWebhook"
# response = requests.post(url)
# print(response.json())
#
# url = f"https://api.telegram.org/bot{TG_API_KEY}/getWebhookInfo"
#
# response = requests.get(url)
