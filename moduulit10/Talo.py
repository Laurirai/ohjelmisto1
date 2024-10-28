from Hissi import Hissi

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissi_maara = hissi_maara
        self.hissi_lista = []

        for i in range(hissi_maara):
            self.hissi_lista.append(Hissi(self.alin_kerros, self.ylin_kerros))


    def aja_hissia(self, hissin_num, kohdekerros):
        print(f"Hissin numero: {hissin_num}")
        self.hissi_lista[hissin_num - 1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit käsketään alimpaan kerrokseen...")
        hissin_lkm = 1
        for hissi in self.hissi_lista:
            print(f"Hissi num {hissin_lkm} siirtyy nyt alimpaan kerrokseen")
            hissi.siirry_kerrokseen(self.alin_kerros)
            hissin_lkm += 1