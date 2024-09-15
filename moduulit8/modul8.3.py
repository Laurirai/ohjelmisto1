from geopy import distance
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )

def hae_lentokentta_koord(icao):
    kursori = yhteys.cursor()
    sql = f"SELECT latitude_deg,longitude_deg FROM airport WHERE ident LIKE %s"
    kursori.execute(sql, (icao,))
    return kursori.fetchall()

icao1 = input("Anna icao1: ")
coord1 = hae_lentokentta_koord(icao1)
icao2 = input("Anna icao2: ")
coord2 = hae_lentokentta_koord(icao2)

print(distance.distance(coord1[0], coord2[0]).km.__round__(2),"km")


