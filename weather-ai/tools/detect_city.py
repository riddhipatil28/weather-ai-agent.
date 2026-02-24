import requests

API_KEY = "e26cb0b72a6e014686d7370986b95922"

def detect_city(user_message, memory):

    words = user_message.split()

    for w in words:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={w}&appid={API_KEY}"
        res = requests.get(url).json()

        if res.get("cod") == 200:
            memory.set("city", w)
            return w

    # fallback to remembered city
    return memory.get("city")
