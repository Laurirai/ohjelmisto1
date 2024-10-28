class Julkaisu:
    def __init__(self, name):
        self.name = name


class Kirja(Julkaisu):
    def __init__(self, name, sivu_m, kirjoittaja):
        super().__init__(name)
        self.name = name
        self.sivu_m = sivu_m
        self.kirjoittaja = kirjoittaja

    def tulosta_tiedot(self):
        print(f"Teoksen {self.name} on kirjoittanut {self.kirjoittaja}.")
        print(f"Teos sisältää {self.sivu_m} sivua.")

class Lehti(Julkaisu):
    def __init__(self, name, paa_toimittaja):
        super().__init__(name)
        self.name = name
        self.paa_toimittaja = paa_toimittaja

    def tulosta_tiedot(self):
        print(f"Lehden {self.name} on julkaissut {self.paa_toimittaja}.")