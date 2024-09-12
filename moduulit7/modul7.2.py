nimet = set()

while True:
    uus_nimi = input("Anna nimi: ")
    if uus_nimi == "":
        break
    elif uus_nimi not in nimet:
        nimet.add(uus_nimi)
        print("Uusi nimi")
    elif uus_nimi in nimet:
        print("Aiemmin syötetty nimi")

for i in nimet:
    print(i)

