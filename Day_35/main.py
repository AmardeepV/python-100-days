import requests
import os

api_key = os.environ.get("OPEN_WEATHER_MAP_API")
parameters = {
    "appid": api_key,
    "lat": 47.076668,
    "lon": 15.421371,
    "cnt": 4
}

responce = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=parameters)
responce.raise_for_status()
data = responce.json()
will_rain = False
for data in data['list']:
    confition_code = data['weather'][0]['id']
    print(f"weather id: {confition_code}")

    if confition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
