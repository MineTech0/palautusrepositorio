from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):

    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
