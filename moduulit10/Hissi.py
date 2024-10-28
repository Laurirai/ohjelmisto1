class Hissi:
    def __init__(self, alin = 0, ylin = 10, floor = 0):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.kerros = floor

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Nykyinen kerros on : {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Nykyinen kerros on : {self.kerros}")
        if self.kerros < 0:
            self.kerros = 0

    def siirry_kerrokseen(self, num):
        if num > self.kerros:
            for i in range(num - self.kerros):
                self.kerros_ylos()
        elif num < self.kerros:
            for i in range(self.kerros - num):
                self.kerros_alas()