pieni = None
suuri = None

while True:

    uusi = input('Anna luku:')

    if uusi == '':
        break
    if  suuri is None or uusi > suuri:
        suuri = uusi
    elif pieni is None or uusi < pieni:
        pieni = uusi
print(f'isoin {suuri} ja pienin {pieni}')
