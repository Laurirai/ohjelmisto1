from Julkaisu import *

def main():
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("n:o 6", 200, "Rosa Liksom")
    lehti.tulosta_tiedot()
    print("")
    kirja.tulosta_tiedot()


if __name__ == '__main__':
    main()