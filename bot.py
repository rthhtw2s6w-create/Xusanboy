import os
import time
import requests
from flask import Flask
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_me():
    r = requests.get(f"{BASE_URL}/getMe")
    print(r.text, flush=True)

if not BOT_TOKEN:
    print("BOT_TOKEN topilmadi")
    exit()

get_me()

def bot_loop():
    while True:
        print("Bot ishlayapti...", flush=True)
        time.sleep(60)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot ishlayapti"

def run_web():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_web).start()

bot_loop()
