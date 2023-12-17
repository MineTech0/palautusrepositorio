from kivi_paperi_sakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        _toisen_siirto = input("Toisen pelaajan siirto: ")
        return _toisen_siirto

