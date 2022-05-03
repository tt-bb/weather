import requests
from geopy.geocoders import Nominatim
from datetime import datetime
from env import API_KEY


# Get coordinates from city
geolocator = Nominatim(user_agent="MyApp")
city_name = input("Enter a city Name : ")
location = geolocator.geocode(city_name)

# Get JSON
key = API_KEY
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
exclude = "minutely,hourly,alerts"
url = f"{base_url}lat={location.latitude}&lon={location.longitude}&exclude={exclude}&appid={key}&units=metric"
weather_data = requests.get(url).json()
daily = weather_data["daily"]

# Print forecast for 5 days
for i in range(0, 5):
    time = datetime.fromtimestamp(daily[i]["dt"]).strftime("%d-%m-%y")
    feels_day = daily[i]["feels_like"]["day"]
    feels_night = daily[i]["feels_like"]["night"]
    weather = daily[i]["weather"][0]["main"]
    print(f"Forecast for : {time}")
    print(f"\tFeels like day : {feels_day}°C")
    print(f"\tFeels like night : {feels_night}°C")
    print(f"\tWeather : {weather}")
