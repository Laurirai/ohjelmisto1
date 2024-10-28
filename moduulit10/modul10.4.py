from Kilpailu import Kilpailu
from Auto import Auto
import random

def main():
    minun_kilpailu = Kilpailu("Suuri romuralli", 8000)
    kilpailu_meneillaan = True

    autot_lista = []
    for i in range(1, 11):
        max_nopeus = random.randint(100, 200)
        rekkari = f"ABC-{i}"
        minun_kilpailu.autot_lista.append(Auto(rekkari, max_nopeus))

    while kilpailu_meneillaan:
        minun_kilpailu.tunti_kuluu()
        if minun_kilpailu.tunnit % 10 == 0:
            print("Tämän hetkinen tilanne on seuraava: ")
            print("")
            minun_kilpailu.tulosta_tilanne()

        if minun_kilpailu.kilpailu_ohi():
            kilpailu_meneillaan = False

    print("Kilpailu ohi...")
    print(" ")
    minun_kilpailu.tulosta_tilanne()



if __name__ == '__main__':
    main()