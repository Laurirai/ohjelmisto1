import requests
import json

haku = "https://api.chucknorris.io/jokes/random"


try:
    vastaus = requests.get(haku)
    if vastaus.status_code==200:
        print(vastaus.json()['value'])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")