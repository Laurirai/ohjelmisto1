suku = input('Anna sukupuoli (M/N) :')
hemo = int(input('Anna hemoglobiiniarvo:'))

if suku == 'M':
    if hemo > 195:
        print('Arvo korkea')
    elif hemo < 134:
        print('Arvo alhainen')
    else:
        print('Arvo normaali')
elif suku == 'N':
    if hemo > 175:
        print('Arvo korkea')
    elif hemo < 117:
        print('Arvo alhainen')
    else:
        print('Arvo normaali')
else:
    print('Oletko alieni?')
