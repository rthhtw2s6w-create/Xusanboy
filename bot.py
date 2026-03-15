import requests

BOT_TOKEN = "8506497703:AAHfZYwYmfYZsterD2wL1KMK4IsLAvXwKiM"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_me():
    url = f"{BASE_URL}/getMe"
    response = requests.get(url)
    print(response.text)

get_me()
