# Weather App

A Python web app that shows live weather for several cities, using data from the OpenWeatherMap API.

## What it does
- Fetches current temperature and weather descriptions from a live API
- Displays each city in a styled card with hover animations

## Built with
- Python and Flask
- OpenWeatherMap API (REST, JSON)
- Jinja2 templates
- HTML and Tailwind CSS
- python-dotenv (to keep the API key private)

## How to run it
1. Install the packages: `pip install flask requests python-dotenv`
2. Get a free API key from openweathermap.org
3. Create a `.env` file in the project folder and add your key to it (see `app.py` for the variable name)
4. Run `python app.py` and open http://127.0.0.1:5000