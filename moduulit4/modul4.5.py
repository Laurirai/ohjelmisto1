kayttis = 'python'
salis = 'rules'

luku = 1

while luku < 6:
    yritys = input('Käyttäjätunnus: ')
    yritys1 = input('Salasana: ')
    if yritys == kayttis and yritys1 == salis:
        print('Tervetuloa')
        break
    elif yritys != kayttis and yritys1 == salis:
        luku += 1
        continue
    elif yritys == kayttis and yritys1 != salis:
        luku += 1
        continue
    else:
        print('Uusi yritys')
        luku += 1
        continue

if luku == 6:
    print('Pääsy evätty')
