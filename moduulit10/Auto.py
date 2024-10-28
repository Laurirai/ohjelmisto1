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