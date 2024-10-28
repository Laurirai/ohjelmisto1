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

    def uusi_nopeus(self, uusi_lukema):
        if uusi_lukema <= self.huippunopeus:
            self.taman_hetkinen_nopeus = uusi_lukema
        else:
            self.taman_hetkinen_nopeus = self.huippunopeus

class SahkoAuto(Auto):
    def __init__(self, rekisteri_tunnus, huippunopeus, akku_kw_h):
        super().__init__(rekisteri_tunnus, huippunopeus)
        self.akku_kw_h = akku_kw_h

class PolttomoottoriAuto(Auto):
    def __init__(self, rekisteri_tunnus, huippunopeus, bensatankki_l):
        super().__init__(rekisteri_tunnus, huippunopeus)
        self.bensatankki_l = bensatankki_l
