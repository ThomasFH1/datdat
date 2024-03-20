from .brukerhistorie_2 import Brukerhistorie2
from .brukerhistorie_3 import Brukerhistorie3
from .brukerhistorie_4 import Brukerhistorie4
from .brukerhistorie_5 import Brukerhistorie5
from .brukerhistorie_6 import Brukerhistorie6


class BrukerhistorieHandler:
    def __init__(self, teater_id, db_file_path):
        self.brukerhistorier = {
            2: Brukerhistorie2(teater_id, db_file_path),
            3: Brukerhistorie3(teater_id, db_file_path),
            4: Brukerhistorie4(teater_id, db_file_path),
            5: Brukerhistorie5(teater_id, db_file_path),
            6: Brukerhistorie6(teater_id, db_file_path),
        }

    def brukerhistorier(self, historienummer):
        try:
            historienummer = int(historienummer)
        except ValueError:
            raise ValueError("Brukerhistorienummer må være et heltall")

        if historienummer not in self.brukerhistorier:
            raise ValueError(
                "Ugyldig brukerhistorienummer. Gyldige verdier er 2 til 6.")

        brukerhistorie = self.brukerhistorier[historienummer]
        brukerhistorie.full_brukerhistorie()
