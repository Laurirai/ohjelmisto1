import random
from contextlib import nullcontext


def funktio():
    randomi = random.randrange(1, 7)
    return randomi

luku = 0

while True:
    luku = funktio()
    if luku == 6:
        print(luku)
        break
    else:
        print(luku)
