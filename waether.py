import requests 

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

cites = ["Guadalajara, MX", "Mexico City, MX", "London, GB", "Paris, FR", "New York, US", "Madrid, ES", "Barcelona, ES", "Tokyo, JP"]

for city in cites:
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + api_key
    response = requests.get(url)
    data = response.json()
    temperature = data["main"]["temp"]
    print(f"The temperature in {city} is {temperature}°C")