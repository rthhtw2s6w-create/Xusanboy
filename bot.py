import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_me():
    r = requests.get(f"{BASE_URL}/getMe")
    print(r.text, flush=True)

if not BOT_TOKEN:
    print("BOT_TOKEN topilmadi")
    exit()

get_me()

while True:
    print("Bot ishlayapti...", flush=True)
    time.sleep(60)
