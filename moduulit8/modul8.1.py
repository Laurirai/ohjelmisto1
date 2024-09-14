import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )
def hae_lentokentta(icao):
    kursori = yhteys.cursor()

    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))

    rivi = kursori.fetchone()
    if rivi:
        nimi, sijaintikunta = rivi
        print(f"Lentoaseman nimi: {nimi}, sijaintikunta: {sijaintikunta}")
    else:
        print(f"Lentoasemaa ICAO-koodilla {icao} ei löytynyt")

    kursori.close()

koodi = input("Syötä lentoaseman ICAO_koodi: ")
hae_lentokentta(koodi)
