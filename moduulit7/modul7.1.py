vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")

num = int(input("Anna kuukauden numero: "))

if num == 1 or num == 2 or num == 12:
    print("Talvi")
elif num == 3 or num == 4 or num == 5:
    print("Kevät")
elif num == 6 or num == 7 or num == 8:
    print("Kesä")
else:
    print("Syksy")

