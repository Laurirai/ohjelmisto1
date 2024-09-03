import math

def pinta_ala(halkaisija, hinta):
    sade = halkaisija / 2
    alue = sade * sade * math.pi
    raha = hinta / alue
    return raha

if __name__ == "__main__":
    eka_halk = int(input('Anna ensimmäisen pitsan halkaisija: '))
    eka_hint = int(input('Anna ensimmäisen pitsan hinta: '))

    toka_halk = int(input('Anna toisen pitsan halkaisija: '))
    toka_hint = int(input('Anna toisen pitsan hinta: '))

    eka_tulos = pinta_ala(eka_halk, eka_hint)
    toka_tulos = pinta_ala(toka_halk, toka_hint)
    if eka_tulos < toka_tulos:
        print('Ensimmäisen pitsan hinta on parempi')
    else:
        print('Toisen pitsan hinta on parempi')
