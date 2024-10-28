from Talo import Talo
from Auto import Auto
import random

class Kilpailu:
    def __init__(self, Kilpailun_nimi, pituus_km):
        self.Kilpailun_nimi = Kilpailun_nimi
        self.pituus_km = pituus_km
        self.autot_lista = []
        self.tunnit = 0

    def tunti_kuluu(self):
        for auto in self.autot_lista:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)
        self.tunnit += 1

    def tulosta_tilanne(self):
        self.autot_lista.sort(key=lambda auto: auto.kuljettu_matka, reverse=True)
        for auto in self.autot_lista:
            print(f'Rekisteri: {auto.rekisteri_tunnus}, Kuljettu matka: {auto.kuljettu_matka:.2f} km')
        print("")

    def kilpailu_ohi(self):
        for auto in self.autot_lista:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False
