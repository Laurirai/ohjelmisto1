import random

class Auto:
    def __init__(self, rekisteri_tunnus, huippunopeus, taman_hetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippunopeus = huippunopeus
        self.taman_hetkinen_nopeus = taman_hetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, nopeus):
        self.taman_hetkinen_nopeus += nopeus
        if self.taman_hetkinen_nopeus > self.huippunopeus:
            self.taman_hetkinen_nopeus = self.huippunopeus
        elif self.taman_hetkinen_nopeus < 0:
            self.taman_hetkinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.taman_hetkinen_nopeus * tunnit

# Luo lista Auto-olioista
autot_lista = []
for i in range(1, 11):
    max_nopeus = random.randint(100, 200)
    rekkari = f"ABC-{i}"
    autot_lista.append(Auto(rekkari, max_nopeus))

# Simuloidaan ajaminen
kilpailu_ohi = False
while not kilpailu_ohi:
    for auto in autot_lista:
        vauhtimuutos = random.randint(-10, 15)
        auto.kiihdyta(vauhtimuutos)
        auto.kulje(1)

        # Päättyy, kun ensimmäinen auto saavuttaa vähintään 1000 km
        if auto.kuljettu_matka >= 1000:
            kilpailu_ohi = True
            break

# Lajitellaan autot kuljetun matkan perusteella suurimmasta pienimpään
autot_lista.sort(key=lambda auto: auto.kuljettu_matka, reverse=True)

# Tulostetaan tulokset
for auto in autot_lista:
    print(f'Rekisteri: {auto.rekisteri_tunnus}, Kuljettu matka: {auto.kuljettu_matka:.2f} km')
