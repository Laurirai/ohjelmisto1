luokka = input('Anna hyttiluokka(LUX, A, B, C):')

if luokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella')
elif luokka == 'A':
    print('A on ikkunallinen hytti autokanne yläpuolella')
elif luokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella')
elif luokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka')
