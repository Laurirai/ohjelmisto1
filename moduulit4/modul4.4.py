import random

rand = random.randrange(1, 10)

while True:
    arvaus = int(input('Arvaa luku: '))
    if arvaus == rand:
        print('Oikein')
        break
    elif arvaus < rand:
        print('Liian pieni arvaus')
        continue
    else:
        print('Liian suuri arvaus')
        continue
