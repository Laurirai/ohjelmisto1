leivit = int(input('Anna leiviskät: '))
naulat = int(input('Anna naula: '))
luodit = float(input('Anna luodit: '))

luoti = float(luodit * 13.3)
naula = float(naulat * 32 * 13.3)
leivi = float(leivit * 20 * 32 * 13.3)

kaikki_grammat = luoti + naula + leivi




kilot = int(kaikki_grammat // 1000)
grammat = kaikki_grammat % 1000

print(f'{kilot} Kiloa ja {grammat} grammaa')
