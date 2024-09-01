tuumat = 1
while tuumat > 0:
    tuumat = int(input('Anna tuumat:'))
    if tuumat < 0:
        break

    cent = tuumat * 2.54
    print(cent)