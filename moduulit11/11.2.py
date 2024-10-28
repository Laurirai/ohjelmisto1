from UusiAuto import *

def main():
    sahko_auto = SahkoAuto("ABC-15", 180, 52.5)
    bensa_auto = PolttomoottoriAuto("ACD-123", 165, 32.3)

    sahko_auto.uusi_nopeus(130)
    bensa_auto.uusi_nopeus(160)

    sahko_auto.kulje(3)
    bensa_auto.kulje(3)

    print(f"Sähköauton {sahko_auto.rekisteri_tunnus} mittarilukema on: {sahko_auto.kuljettu_matka} km")
    print(f"Polttomoottoriauton {bensa_auto.rekisteri_tunnus} mittarilukema on: {bensa_auto.kuljettu_matka} km")




if __name__ == '__main__':
    main()