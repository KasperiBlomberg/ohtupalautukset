KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        def validate_positive_int(value, name):
            if not isinstance(value, int) or value < 0:
                raise Exception(f"Väärä {name}")

        validate_positive_int(kapasiteetti, "kapasiteetti")
        validate_positive_int(kasvatuskoko, "oletuskasvatus")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self.alkioiden_lkm == len(self.ljono):
            self.kasvata_listaa()

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1            

    def kasvata_listaa(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1

    def kopioi_lista(self, a, b):
        b[:len(a)] = a

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        res = self._luo_lista(self.alkioiden_lkm)
        for i in range(self.alkioiden_lkm):
            res[i] = self.ljono[i]
        return res

    @staticmethod
    def yhdiste(a, b):
        res = IntJoukko()
        for number in set(a.ljono + b.ljono):
            res.lisaa(number)
        return res

    @staticmethod
    def leikkaus(a, b):
        res = IntJoukko()
        for number in set(a.ljono) & set(b.ljono):
            res.lisaa(number)
        return res

    @staticmethod
    def erotus(a, b):
        res = IntJoukko()
        for number in set(a.ljono) - set(b.ljono):
            res.lisaa(number)
        return res

    def __str__(self):
        return f"{{{', '.join([str(number) for number in self.ljono[:self.alkioiden_lkm]])}}}"
