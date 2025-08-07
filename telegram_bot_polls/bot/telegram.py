import requests

TELEGRAM_TOKEN = "8205636056:AAGkwohUaw7HGtRT55kB6yIry15jweEmm4g"
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    return response

def send_poll(chat_id, poll):
    url = f"{BASE_URL}/getPoll"
    payload = {
        "chat_id": chat_id,
        "question": poll.question,
        "options": poll.options,
        "is_anonymous": False
    }
    response = requests.post(url, json=payload)
    if "result" in response.json():
            poll.poll_id = response["result"]["poll"]["id"]
            poll.save()
    return response