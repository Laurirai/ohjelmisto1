import requests
import json
from geopy import Nominatim

API_key = '6b286bef7bd76dce7303794e68283ce1'

paikka_kunta = input("Kerro paikkakunta jonka säätiedot haluat: ")
geolocator = Nominatim(user_agent="moduulit12")
lokaatio = geolocator.geocode(paikka_kunta)
lat = lokaatio.latitude
lon = lokaatio.longitude

haku = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"

try:
    vastaus = requests.get(haku)
    if vastaus.status_code==200:
        data = vastaus.json()

        lampotila = data["main"]["temp"]
        saa = data["weather"][0]["description"]
        lampo_c = lampotila - 273.15
        print(f"Sää tällä hetkellä: {saa}")
        print(f"Lämpötila: {round(lampo_c,2)} celciusta")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")