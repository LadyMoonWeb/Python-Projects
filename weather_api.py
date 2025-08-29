import requests
import os
import argparse

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Погода в {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
    else:
        print("Ошибка при получении данных")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", default="Bishkek")
    parser.add_argument("--api-key", default=os.environ.get("OPENWEATHER_API_KEY"))
    args = parser.parse_args()
    get_weather(args.city, args.api_key)
