pituus = int(input('Anna kuhan mitta:'))

if pituus >= 37:
    print('Kala on hyvän kokoinen')
else:
    vali = 37 - pituus
    print(f'Sinun pitää laskea kala takaisin. Pituudesta puuttuu {vali}centtiä')