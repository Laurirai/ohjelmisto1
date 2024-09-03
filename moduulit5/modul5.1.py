import random
summa = 0
monta = int(input('Anna arpojen määrä: '))
for i in range(monta):
    summa += random.randrange(1, 6)

print(summa)