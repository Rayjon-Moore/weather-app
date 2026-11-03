from flask import Flask, render_template, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

api_key = os.getenv("API_KEY")

@app.route("/")
def home():
    cites = ["Guadalajara, MX", "Mexico City, MX", "London,GB", "Paris, FR", "New York, US", "Madrid, ES", "Barcelona, ES", "Tokyo, JP"]
    weather_data = []
    for city in cites:
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + api_key
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        weather_data.append(f"{city}: {temperature}°C, {description}")
    return render_template("index.html", weather_data=weather_data)

@app.route('/weather')
def get_weather():
    data = {"city": "London", "temperature": 18}
    return jsonify(data)

@app.route('/hello')
def function_here():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

