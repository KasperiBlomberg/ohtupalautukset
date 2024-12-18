from kivi_paperi_sakset import KiviPaperiSakset


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        peli = KiviPaperiSakset.luo_peli(vastaus)
        if peli is None:
            break
        peli.pelaa()


if __name__ == "__main__":
    main()
