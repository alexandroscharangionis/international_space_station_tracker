import requests
from datetime import datetime


MY_LATITUDE = 44.426765
MY_LONGITUDE = 26.102537

# Parameters needed for sunrise-sunset API request:
location_parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

# Make request and get response from API endpoint:
response = requests.get(
    "https://api.sunrise-sunset.org/json", params=location_parameters)

# Raise exception for unsuccessful status code (anything other than 200)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
