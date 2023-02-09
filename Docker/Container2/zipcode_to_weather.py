# explore the Open Weather dot Org API at: https://openweathermap.org/api

from datetime import datetime
import requests
from flask import Flask, request


app = Flask(__name__)


# Hardcoded zip code to weather mapping
weather_data = {
    "10025": "Cloudy",
    "90011": "Cloudy",
    "60601": "Sunny",
    "95035": "Sunny",
	"75034": "Heavy Snow",
	"79936": "Rain",
	"77084": "Rain",
	"11211": "Fog",
	"90805": "Fog",
	"10456": "Blizzard",
	"75217": "Blizzard",
	"93727": "Snow",
	"94112": "Cloudy",
	"95133": "Overcast",
	"92126": "Overcast"
}

@app.route("/zipweather")
def get_weather():
    zip_code = request.args.get("zip_code")
    weather = weather_data.get(zip_code, "Not available")
    return f"<h3>Zip code: {zip_code}</h3><br><h3>Weather: {weather}</h3>"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 8001, debug = True)
