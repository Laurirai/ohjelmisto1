import random
from contextlib import nullcontext


def funktio(annettu):
    randomi = random.randint(1, annettu)
    return randomi

luku = 0
annettu = int(input('Anna nopan sivujenmäärä: '))

while True:

    luku = funktio(annettu)
    print(luku)
    if luku == annettu:
        break

