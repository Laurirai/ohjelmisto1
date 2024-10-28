import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='demogame',
    user='root',
    password='',
    autocommit=True
)


def alustetaan_taulu():
    sql = "INSERT INTO pelaaja (id, nimi, raha, kokemus, omistetut_koneet, tehdyt_keikat, bensa) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = ("1", "John", "500", "0", "0", "0", "0")

    mycursor = yhteys.cursor()
    mycursor.execute(sql, val)
    yhteys.commit()
    mycursor.close()

def paivitus():

    mycursor = yhteys.cursor()

    sql = f"UPDATE pelaaja  SET nimi = '{pelaajan_nimi}', raha ='{pelaajan_rahat}', omistetut_koneet ='{pelaajan_omistamat_koneet_maara}', kokemus ='{pelaajan_kokemuspisteet}', tehdyt_keikat = '{tehdyt_keikat}', bensa = '{omistamat_bensa_kanisterit}'  WHERE id = '1'"

    mycursor.execute(sql)

    yhteys.commit()
    mycursor.close()


pelaajan_nimi = input("Anna nimi: ")

alustetaan_taulu()
viron_koneen_bensa_tilavuus = 5
pelaajan_rahat = 500
pelaajan_kokemuspisteet = 0
pelaajan_omistamat_koneet_maara = 0
pelaajan_omistamat_koneet_lista = []
tehdyt_keikat = 0
omistamat_bensa_kanisterit = 0
bensan_hinta = 100
viron_keikan_palkka = 500
viron_keikan_kokemuspisteet = 500
viron_keikka_lista = ["Viron keikka", "Matkaa: ", f"Palkka: {viron_keikan_palkka}", f"Kokemuspisteet: {viron_keikan_kokemuspisteet}"]
keikat_lista1 = ["[1] Viron keikka", "[2] Turun keikka", "[3] Latvian keikka", "[4] Tanskan keikka",
                 "[5] Puolan keikka", "[6] Saksan keikka"]
keikat_lista2 = ["[7] Tšekin keikka", "[8] Britannian keikka", "[9] Islannin keikka", "[10] Espanjan keikka",
                 "[11] Egyptin keikka"]
keikat_lista3 = ["[12] Dubain keikka", "[13] Intian keikka", "[14] Amerikan keikka", "[15] Japanin keikka",
                 "[16] Etelä-Afrikan keikka"]
keikat_lista4 = ["[17] Brasilian keikka", "[18] Argentinan keikka", "[19] Bora Bora saarten keikka",
                 "[20] Uuden-Seelannin keikka"]
lentokone_lista = ["[1]Pienen matkan lentokone", "[2]Keskipitkän matkan lentokone", "[3]Pitkän matkan rahti-lentokone",
                   "[4]Raketti", "[5]Kanisteri-bensaa"]
pien_matkan_lentokone = ["Nimi: ATR-72", "Kulutus: 2 kanisteria per 200km","Tankin tilavuus 4 kanisteria", f"Koneeseen mahtuu {viron_koneen_bensa_tilavuus} kanisteria", "Hinta: 250€"]
kaupan_kanisteri = ["Perus bensaa", "Hinta 100€"]
pien_matkan_lentokone_kulutus = 2
keskipitkan_matkan_lentokone = ["Nimi: Embraer C-390", "Kulutus: ", "Hinta: 1000€"]
keskipitkan_matkan_lentokone_kulutus = 4
pitkanmatkan_rahtilentokone = ["Nimi: ", "Kulutus: ", "Hinta: "]
pitkanmatkan_rahtilentokone_kulutus = 6
raketti = ["Nimi: Melon Rusk StarShip", "Kulutus: --", "Hinta: "]
paivitus()


def hae_aloitus_koorinaatit():
    kursori = yhteys.cursor()
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EFHK'"
    kursori.execute(sql)
    suomi_koord = kursori.fetchall()
    return suomi_koord


aloitus_koordinaatit = hae_aloitus_koorinaatit()


def hae_viron_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EETN'"
    kursori.execute(sql)
    viro_koord = kursori.fetchall()
    return viro_koord


viron_koordinaatit = hae_viron_lentokentta_ja_koordinaatisto()
suomi_viro_vali = round(distance.distance(aloitus_koordinaatit[0], viron_koordinaatit[0]).km, 2)


def hae_turun_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EFTU'"
    kursori.execute(sql)
    turku_koord = kursori.fetchall()
    return turku_koord


turun_koordinaatit = hae_turun_lentokentta_ja_koordinaatisto()


def hae_latvian_lentokentta_ja_koordinatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EVRA'"
    kursori.execute(sql)
    latvia_koord = kursori.fetchall()
    return latvia_koord


latvian_koordinaatit = hae_latvian_lentokentta_ja_koordinatisto()


def hae_tanskan_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EKCH'"
    kursori.execute(sql)
    tanska_koord = kursori.fetchall()
    return tanska_koord


tanskan_koordinaatit = hae_tanskan_lentokentta_ja_koordinaatisto()


def hae_puolan_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EPWA'"
    kursori.execute(sql)
    puola_koord = kursori.fetchall()
    return puola_koord


puolan_koordinaatit = hae_puolan_lentokentta_ja_koordinaatisto()


def hae_saksan_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EDDB'"
    kursori.execute(sql)
    saksa_koord = kursori.fetchall()
    return saksa_koord


saksan_koordinaatit = hae_saksan_lentokentta_ja_koordinaatisto()


def hae_Tšekin_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'LKPR'"
    kursori.execute(sql)
    tšekki_koord = kursori.fetchall()
    return tšekki_koord


tšekin_koordinaatit = hae_Tšekin_lentokentta_ja_koordinaatisto()


def hae_britannian_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EGLL'"
    kursori.execute(sql)
    britannia_koord = kursori.fetchall()
    return britannia_koord


britannia_koordinaatit = hae_britannian_lentokentta_ja_koordinaatisto()


def hae_islannin_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'BIKF'"
    kursori.execute(sql)
    islanti_koord = kursori.fetchall()
    return islanti_koord


islanti_koordinaatit = hae_islannin_lentokentta_ja_koordinaatisto()


def hae_espanjan_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'LEMD'"
    kursori.execute(sql)
    espanja_koord = kursori.fetchall()
    return espanja_koord


espanja_koordinaatit = hae_espanjan_lentokentta_ja_koordinaatisto()


def hae_egyptin_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'HECA'"
    kursori.execute(sql)
    egypti_koord = kursori.fetchall()
    return egypti_koord


egypti_koordinaatit = hae_egyptin_lentokentta_ja_koordinaatisto()


def hae_dubain_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'OMDB'"
    kursori.execute(sql)
    dubai_koord = kursori.fetchall()
    return dubai_koord


dubai_koordinaatit = hae_dubain_lentokentta_ja_koordinaatisto()


def hae_intian_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'EGLL'"
    kursori.execute(sql)
    intia_koord = kursori.fetchall()
    return intia_koord


intia_koordinaatit = hae_intian_lentokentta_ja_koordinaatisto()


def hae_amerikan_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'KJFK'"
    kursori.execute(sql)
    amerikka_koord = kursori.fetchall()
    return amerikka_koord


amerikka_koordinaatit = hae_amerikan_lentokentta_ja_koordinaatisto()


def hae_japanin_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'RJAA'"
    kursori.execute(sql)
    japani_koord = kursori.fetchall()
    return japani_koord


japani_koordinaatit = hae_japanin_lentokentta_ja_koordinaatisto()


def hae_Eafrikka_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'FACT'"
    kursori.execute(sql)
    Eafrikka_koord = kursori.fetchall()
    return Eafrikka_koord


Eafrikan_koordnaatit = hae_Eafrikka_lentokentta_ja_koordinaatisto()


def hae_brasilian_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'SBGL'"
    kursori.execute(sql)
    brasilia_koord = kursori.fetchall()
    return brasilia_koord


brasilian_koordinaatit = hae_brasilian_lentokentta_ja_koordinaatisto()


def hae_argentinan_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'SAEZ'"
    kursori.execute(sql)
    argentina_koord = kursori.fetchall()
    return argentina_koord


argentinan_koordinaatit = hae_argentinan_lentokentta_ja_koordinaatisto()


def hae_borabora_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'NTTB'"
    kursori.execute(sql)
    borabora_koord = kursori.fetchall()
    return borabora_koord


boraboran_koordinaatit = hae_borabora_lentokentta_ja_koordinaatisto()


def hae_Useelanti_lentokentta_ja_koordinaatisto():
    kursori = yhteys.cursor()
    ## SQL haku
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident LIKE 'NZWN'"
    kursori.execute(sql)
    Useelanti_koord = kursori.fetchall()
    return Useelanti_koord


Useelanti_koordinaatit = hae_Useelanti_lentokentta_ja_koordinaatisto()


def aloita_peli():
    while True:
        print("***CARGO SIMULATOR***")
        print("")
        print("")
        print("[1] Uusi peli")
        print("[2] Sulje sovellus")
        print("")
        valinta = input("Valitse 1,2: ")
        print("")
        if valinta == "1":
            peli_alkaa_tarina()

        elif valinta == "2":
            print("Suljetaan sovellus...")
            break
        else:
            print("Valitse painaen numeronäppäintä ja enter")
            print("")

def peli_alkaa_tarina():
    while True:
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
        pelin_paa_valikko()


def pelin_paa_valikko():
    while True:
        print("")
        print("[1] Keikat")
        print("[2] Kauppa")
        print("[3] Status")
        print("[4] Sulje sovellus")
        print("")
        valinta = input("Valitse 1,2,3,4: ")
        if valinta == "1":
            keikat()
        elif valinta == "2":
            kauppa()
        elif valinta == "3":
            status()
        elif valinta == "4":
            print("Suljetaan sovellus...")
            exit()
        else:
            print("Valitse painaen numeronäppäintä ja enter")
            print("")
            pelin_paa_valikko()


def keikat():
    while True:
        print("")
        kursori = yhteys.cursor()

        sql = "SELECT omistetut_koneet, tehdyt_keikat FROM pelaaja WHERE id = 1"
        kursori.execute(sql)

        tulokset = kursori.fetchall()
        kursori.close()
        if tulokset:
            omistetut_koneet, tehdyt_keikat = tulokset[0]
            if omistetut_koneet == 0:
                print("Et ole vielä ostanut konetta. Painamalla 'p' ja enter pääset takaisin pää-valikkoon.")
                ilman_konetta_valinta = input(":")
                if ilman_konetta_valinta == "p":
                    pelin_paa_valikko()
                else:
                    print("Luku taito ei selvästi koske sinua...")
            elif omistetut_koneet > 0:
                if tehdyt_keikat == 0:
                    print("Tekemällä tämän keikan saat kokemuspisteitä ja uusia keikkoja auki")
                    for i in viron_keikka_lista:
                        print("")
                        print(i)
                    vastaus = input("Haluatko keikan?(e/k)")
                    if vastaus == "e":
                        pelin_paa_valikko()
                    elif vastaus == "k":
                        print("Lähdetään keikalle!!")
                    elif vastaus == "p":
                        pelin_paa_valikko()
                    else:
                        print("vastaukseksi käyvät 'e' ja 'k'")



def kauppa():
    while True:

        kursori = yhteys.cursor()

        sql = "SELECT raha FROM pelaaja WHERE id = 1"
        kursori.execute(sql)

        tulokset = kursori.fetchall()
        kursori.close()
        raha = tulokset[0]

        for i in lentokone_lista:
            print("")
            print(i)
        print("Painamalla 6 ja enter pääset takaisin pää-valikkoon")
        valinta = input("Valitse 1,2,3,4,5,6: ")

        if valinta == "1":
            for i in pien_matkan_lentokone:
                print("")
                print(i)
            print("")
            osto_paatos = input("Haluatko ostaa koneen? (e/k)")
            if osto_paatos.lower() == "e":
                kauppa()
            elif osto_paatos.lower() == "k":
                osta_kone(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet,pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit)

        elif valinta == "2":
            for i in keskipitkan_matkan_lentokone:
                print("")
                print(i)
            print("")
            osto_paatos = input("Haluatko ostaa koneen? (e/k): ")
            if osto_paatos.lower() == "e":
                kauppa()
            elif osto_paatos.lower() == "k":
                osta_kone(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara)
        elif valinta == "3":
            for i in pitkanmatkan_rahtilentokone:
                print("")
                print(i)
            print("")
            osto_paatos = input("Haluatko ostaa koneen? (e/k): ")
            if osto_paatos.lower() == "e":
                kauppa()
            elif osto_paatos.lower() == "k":
                osta_kone(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit)
        elif valinta == "4":
            for i in raketti:
                print("")
                print(i)
            print("")
            osto_paatos = input("Haluatko ostaa koneen? (e/k): ")
            if osto_paatos.lower() == "e":
                kauppa()
            elif osto_paatos.lower() == "k":
                osta_kone(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit)
        elif valinta == "5":
            print("")
            for i in kaupan_kanisteri:
                print("")
                print(i)
            haluatko = input("Haluatko ostaa kanisterin? (e/k)")
            if haluatko == "e":
                kauppa()
            elif haluatko == "k":
                bensan_osto(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit)

            else:
                print("Osaatko lukea?")
        elif valinta == "6":
            print("Palataan päävalikkoon...")
            pelin_paa_valikko()
        else:
            print("")
            print("Valitse painaen numeronäppäintä ja enter")
            print("")

def update_sql(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit):
    kursori = yhteys.cursor()
    sql = f"UPDATE pelaaja SET nimi = %s, raha = %s, kokemus = %s, omistetut_koneet = %s, tehdyt_keikat = %s, bensa = %s WHERE id = 1;"
    kursori.execute(sql,(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit))
    yhteys.commit()
    kursori.close()



def bensan_osto(pelaajan_nimi, pelaajan_rahat, pelaajan_omistamat_koneet_maara, pelaajan_kokemuspisteet, tehdyt_keikat, omistamat_bensa_kanisterit):
    kursori = yhteys.cursor()
    sql = f"UPDATE pelaaja SET nimi = %s, raha = raha - 100, kokemus = %s, omistetut_koneet = %s, tehdyt_keikat = %s, bensa = bensa + 1 WHERE id = 1;"
    kursori.execute(sql,(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit))
    yhteys.commit()
    kursori.close()
    pelin_paa_valikko()

def osta_kone(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit):
    print("")
    print("KONE OSTETTU!!")
    print("Otetaan kone käyttöön...")
    print("Katsastut läpi ja valmis keikoille!")
    print("")
    pelaajan_rahat -= 250
    pelaajan_omistamat_koneet_maara += 1

    update_sql(pelaajan_nimi, pelaajan_rahat, pelaajan_kokemuspisteet, pelaajan_omistamat_koneet_maara, tehdyt_keikat, omistamat_bensa_kanisterit)

    pelin_paa_valikko()


def status():
    while True:
        print("***STATUS***")
        kursori = yhteys.cursor()

        sql = "SELECT nimi, raha, omistetut_koneet, kokemus, tehdyt_keikat, bensa FROM pelaaja WHERE id = 1"
        kursori.execute(sql)

        tulokset = kursori.fetchall()
        kursori.close()

        print("")

        if tulokset:
            nimi, raha, omistetut_koneet, kokemus, tehdyt_keikat, bensa = tulokset[0]
            print("")
            print(f"Pelaajan nimi: {nimi}")
            print("")
            print(f"Raha: {raha}")
            print("")
            print(f"Omistetut koneet: {omistetut_koneet}")
            print("")
            print(f"Koneessa bensaa: {bensa} kanisteria")
            print("")
            print(f"Kokemuspisteet: {kokemus}")
            print("")
            print(f"Olet tehnyt: {tehdyt_keikat} keikkaa!!")
            print("")
        else:
            print("Pelaajaa ei löytynyt tai tietoja ei voitu ladata.")

        takaisin = input("Painamalla 'p' ja enter pääset takaisin päävalikkoon...")
        if takaisin.lower() == "p":
            pelin_paa_valikko()
        else:
            print("Osaatko lukea?")

aloita_peli()