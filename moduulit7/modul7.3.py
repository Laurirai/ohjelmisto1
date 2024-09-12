lentoasemat = {}
def syota_uusi_lentoasema():
    icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
    nimi = input("Syötä lentoaseman nimi: ")
    lentoasemat[icao] = nimi
    print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.")

def hae_lentoasema():
    icao = input("Syötä haettavan lentoaseman ICAO-koodi: ").upper()
    if icao in lentoasemat:
        print(f"Lentoaseman nimi ICAO-koodilla {icao} on: {lentoasemat[icao]}")
    else:
        print(f"Lentoasemaa ICAO-koodilla {icao} ei löydy.")

def main():
    while True:
        print("1. Syötä uusi lentoasema")
        print("2. Hae lentoasema")
        print("3. Lopeta ohjelma")
        valinta = input("Anna valintasi (1/2/3): ")
        if valinta == "1":
            syota_uusi_lentoasema()
        elif valinta == "2":
            hae_lentoasema()
        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    main()

