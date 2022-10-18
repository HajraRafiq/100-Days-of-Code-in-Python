import requests
import datetime

MY_LAT = 30.3753205
MY_LONG = 69.345116
parameters = {'lat' : MY_LAT ,
'lng' : MY_LONG,
"formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")
sunset = data["results"]["sunset"].split("T")

print(sunrise)
print(sunrise)