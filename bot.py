import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_me():
    url = f"{BASE_URL}/getMe"
    response = requests.get(url)
    print(response.text)

get_me()
