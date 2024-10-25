import mysql.connector
from geopy import distance


## creating a connection to mysql
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )

def lentaminen(matka):
    if lennettava_tamanhetken_kone == 1:
        print("Lähdetään matkaan!!")





def hae_aloitus_koorinaatit():
    kursori = yhteys.cursor()
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EFHK'"
    kursori.execute(sql)
    suomi_koord = kursori.fetchall()
    return suomi_koord

aloitus_koordinaatit = hae_aloitus_koorinaatit()

## Ensimmäisen keikan lokaation koordinaatiston haku etäisyys laskuja varten
def hae_viron_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EETN'"
    kursori.execute(sql)
    viro_koord = kursori.fetchall()
    return viro_koord




## Tervetuloa peliin
print("***************")
print("CARGO SIMULATOR")
print("***************")
## Avataan peli
painike = input("Paina enter näppäintä aloittaaksesi!!!")
if painike == "":
    print("Avataan CARGO SIMULATOR....")
else:
    print("Paina ENTER näppäintä aloittaaksesi!!!")

## Visuaalista
print("Latautuu...")
print("***************")
print("***************")

## Alustetaan muuttujat
omistetut_koneet = 0
bensa_kanisteri = 150
pelaajan_rahat = 500
pelaajan_kokemuspisteet = 0

## Aloitus valikko
print("Uusi peli[1]")
print("Lataa vanha peli[2]")
valinta = input("Sulje sovellus[3]: ")
print("")

## Peli pyörii while silmukassa
while True:
    if valinta == "1":
        pelaajan_nimi = input("Kerro nimesi: ")
        pelaajan_salasana = input("Luo salasana: ")
        print("")
        break
    elif valinta == "2":
        print("Ladataan vanha tiedosto...")
        kayttis = input("Anna käyttäjä tunnus: ")
        salis = input("Anna salasana: ")
        print("")
    elif valinta == "3":
        break
    else:
        print("")
        print("Voit liikkua valikossa numero näppäimillä. ")


## Lista lentokoneita, joita voidaan ostaa myöhemmin
lentokone_lista = ["Pienen matkan lentokone[1]", "Tilavampi lyhyenmatkan lentokone[2]", "Keskipitkän matkan lentokone[3]", "Keskipitkän matkan rahti-lentokone[4]", "Pitkän matkan rahti-lentokone[5]", "Raketti[6]"]

## Visuaalista ++ tarinaa
print("Latautuu...")
print("***************")
print("***************")
print("Olet herännyt koomasta. Huomaat ettet ole omalla planeetallasi.")
print("Sinulla on hieman rahaa, jolla voit aloittaa oman yrityksesi")
print("Kyseisellä planeetalla ei ole rahti mahdollisuuksia...")
print("Joten päätät perustaa lento-rahtifirman")
print("Haluat päästä pois tältä planeetalta kumppanisi luokse")
print("Ja miksipäs ei.. perustaa samalla avaruuden isoimman lento-rahtifirman..!")
print("")

## Seuraava while silmukka pelin pyörittämiseen
while True:
    if omistetut_koneet < 1:
        print("HINT: Kannattaa käydä kaupassa katsomassa aloituskonetta!")

    ## pelin sisäinen valikko
    print("Keikat[1]")
    print("Kauppa[2]")
    print("Status[3]")
     :alku_valikko
    valikko_valinta = input("Lopeta sovellus[4]: ")
    if valikko_valinta == "1":
        print("")
        print("Keikat")
        print("Viron keikka (Puu tilaus)[1]")
        print("Ruotsin keikka (Lasi tilaus)[2]")
        print("Saksan keikka (Lelu tilaus)[3]")
        keikka_valinta = input("")
        if keikka_valinta == "1":
            print("Viron pien tilaus")
            viro_keikan_maksu = 500
            print("Keikka tarjoaa 500 kokemuspistettä")
            print("Keikka antaa palkkioksi 500€")
            viron_lentokentta = hae_viron_lentokentta_ja_koordinaatisto()
            print(distance.distance(aloitus_koordinaatit[0], viron_lentokentta[0]).km.__round__(2),"km")
            matkan_pituus = distance.distance(aloitus_koordinaatit[0], viron_lentokentta[0]).km.__round__(2)

            haluaako_keikan = input("Otatko keikan vastaan? (e/k)")
            if haluaako_keikan == "e":
                goto alku_valikko
            elif haluaako_keikan == "k":
                lennolle = lentaminen(matkan_pituus)






## Valikko valinnat käyttäjältä
    elif valikko_valinta == "2":

        for i in lentokone_lista:
            print("")
            print(i)
        print("")
        print("Voit palata päävalikkoon painamalla (p)")
        kaupan_sisainen_valinta = input("Mitä konetta haluat tarkastella: ")
        if kaupan_sisainen_valinta == "1":
            print("")
            print("Aloittelevalle rahti yrittäjälle.")
            print("Ei sovellu pitkille matkoille ja isoille rahdeille.")
            print("Kulutus 1 kanisteri per 200")
            print("Hinta 250€")
            osto_paatos = input("Ostatko koneen (k/e): ")
        elif kaupan_sisainen_valinta == "p":
            print("")
            print("Palataan päävalikkoon...")
            input(valikko_valinta)
            if osto_paatos.lower() == "k":
                print("Kone ostettu!!!")
                lennettava_tamanhetken_kone = 1
            elif osto_paatos.lower() == "e":
                print("")
                print("Palataan kauppaan...")
                input(kaupan_sisainen_valinta)
            else:
                print("")
                print("Voit tehdä päätöksen painamalla k/e kirjainta: ")

    elif valikko_valinta == "3":
        print("***STATUS***")
        print("")
        paluu = input("painamalla 'p' voit palata aloitus valikkoon: ")
        if paluu.lower() == "p":
            input(valikko_valinta)
## Poistutaan pelistä
    elif valikko_valinta == "4":
        break
    else:
        print("")
        print("Voit liikkua valikoissa numeronäppäimillä.")
        input(valikko_valinta)



