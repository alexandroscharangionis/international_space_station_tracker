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
sun_response = requests.get(
    "https://api.sunrise-sunset.org/json", params=location_parameters)
iss_response = requests.get("http://api.open-notify.org/iss-now.json")

# Raise exception for unsuccessful status code (anything other than 200)
sun_response.raise_for_status()
iss_response.raise_for_status()

sun_data = sun_response.json()
iss_data = iss_response.json()

# Only save the hour from the entire date format to variables:
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

time_now = datetime.now()
