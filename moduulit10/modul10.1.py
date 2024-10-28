from Hissi import Hissi



def main():

    minun_hissi = Hissi()
    minun_hissi.siirry_kerrokseen(5)
    print(f"Hissin tämän hetkinen kerros : {minun_hissi.kerros}")
    minun_hissi.siirry_kerrokseen(0)
    print(f"Hissin tämän hetkinen kerros : {minun_hissi.kerros}")


if __name__ == '__main__':
    main()
