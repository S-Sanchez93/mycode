#!/usr/bin/env python3
import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
# API_KEY = 'YOUR_API_KEY'
# BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(zip_code):
    params = {
        'zip': f'{zip_code},us',
        'appid': API_KEY,
        'units': 'metric'  # You can change to 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        zip_code = request.form['zip']
        if zip_code:
            weather_data = get_weather_data(zip_code)
    return render_template('weatherapp2.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)

