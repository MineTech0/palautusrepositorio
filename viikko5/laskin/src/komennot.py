class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

    def suorita(self):
        self._sovelluslogiikka.plus(self._syote)
        
class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

    def suorita(self):
        self._sovelluslogiikka.miinus(self._syote)
        
class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

    def suorita(self):
        self._sovelluslogiikka.nollaa()