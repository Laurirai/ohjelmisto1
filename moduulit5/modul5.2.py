lista = []
while True:
    luku = (input('Anna luku: '))
    if luku == '':
        break
    else:
        luku = int(luku)
        lista.append(luku)

lista.sort(reverse=True)
print(lista[:5])



