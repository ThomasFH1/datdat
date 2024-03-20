from .brukerhistorie_2 import Brukerhistorie2
from .brukerhistorie_3 import Brukerhistorie3
from .brukerhistorie_4 import Brukerhistorie4
from .brukerhistorie_5 import Brukerhistorie5
from .brukerhistorie_6 import Brukerhistorie6


class BrukerhistorieHandler:
    def __init__(self, teater_id, db_file_path):
        self.brukerhistorie_2_instance = Brukerhistorie2(
            teater_id, db_file_path)
        self.brukerhistorie_3_instance = Brukerhistorie3(
            teater_id, db_file_path)
        self.brukerhistorie_4_instance = Brukerhistorie4(
            teater_id, db_file_path)
        self.brukerhistorie_5_instance = Brukerhistorie5(
            teater_id, db_file_path)
        self.brukerhistorie_6_instance = Brukerhistorie6(
            teater_id, db_file_path)

    def brukerhistorie(self, historienummer):
        """
        Metode som kjører alle metoder som kreves for en gitt brukerhistorie
        """
        try:
            historienummer = int(historienummer)
        except:
            raise Exception("Brukerhistorienummer må være et heltall")
        if 1 <= historienummer <= 7:
            raise Exception("Brukerhistorienummer må være fra 1 til og med 7")

        if historienummer == 1:
            pass
        elif historienummer == 2:
            self.brukerhistorie_2_instance.full_brukerhistorie()
        elif historienummer == 3:
            self.brukerhistorie_3_instance.full_brukerhistorie()
        elif historienummer == 4:
            self.brukerhistorie_4_instance.full_brukerhistorie()
        elif historienummer == 5:
            self.brukerhistorie_5_instance.full_brukerhistorie()
        elif historienummer == 6:
            self.brukerhistorie_6_instance.full_brukerhistorie()
        elif historienummer == 7:
            pass
