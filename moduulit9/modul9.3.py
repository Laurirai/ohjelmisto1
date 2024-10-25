class Auto:
    def __init__(self, rekisteri_tunnus, huippunopeus, taman_hetkinen_nopeus= 0, kuljettu_matka= 0):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippunopeus = huippunopeus
        self.taman_hetkinen_nopeus = taman_hetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
    def kiihdyta(self, nopeus):
        if nopeus > 0:
            self.taman_hetkinen_nopeus += nopeus
            if self.huippunopeus < self.taman_hetkinen_nopeus:
                self.taman_hetkinen_nopeus = self.huippunopeus
        elif nopeus < 0:
            self.taman_hetkinen_nopeus += nopeus
            if self.taman_hetkinen_nopeus < 0:
                self.taman_hetkinen_nopeus = 0

        else:
            pass

    def kulje(self, tunnit):
        self.kuljettu_matka += self.taman_hetkinen_nopeus * tunnit

eka_auto = Auto('ABC-123', 142, 60, 2000)
eka_auto.kulje(1.5)
print(f'Auton tiedot: Rekkari: {eka_auto.rekisteri_tunnus} Huippunopeus: {eka_auto.huippunopeus} Tämän hetken nopeus: {eka_auto.taman_hetkinen_nopeus} Kuljettu matka: {eka_auto.kuljettu_matka}')
