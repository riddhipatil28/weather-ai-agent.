import requests

API_KEY = "e26cb0b72a6e014686d7370986b95922"

def get_weather(user_message, memory):

    city = memory.get("city")
    if not city:
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    if res.get("cod") != 200:
        return None

    data = {
        "temp": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "pressure": res["main"]["pressure"],
        "wind": res["wind"]["speed"],
        "condition": res["weather"][0]["description"],
        "clouds": res["clouds"]["all"]
    }

    memory.set("weather", data)
    return data
