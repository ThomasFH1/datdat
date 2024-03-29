from miscellaneous.logger import logger

from .brukerhistorie_1 import Brukerhistorie1
from .brukerhistorie_2 import Brukerhistorie2
from .brukerhistorie_3 import Brukerhistorie3
from .brukerhistorie_4 import Brukerhistorie4
from .brukerhistorie_5 import Brukerhistorie5
from .brukerhistorie_6 import Brukerhistorie6
from .brukerhistorie_7 import Brukerhistorie7


class BrukerhistorieHandler:
    def __init__(self, teater_id, db_file_path):
        self.brukerhistorier = {
            1: Brukerhistorie1(teater_id, db_file_path),
            2: Brukerhistorie2(teater_id, db_file_path),
            3: Brukerhistorie3(teater_id, db_file_path),
            4: Brukerhistorie4(teater_id, db_file_path),
            5: Brukerhistorie5(teater_id, db_file_path),
            6: Brukerhistorie6(teater_id, db_file_path),
            7: Brukerhistorie7(teater_id, db_file_path),
        }

    def brukerhistorie(self, historienummer):
        try:
            historienummer = int(historienummer)
        except ValueError:
            logger.error("Brukerhistorienummer må være et heltall")
            return

        if historienummer not in self.brukerhistorier:
            logger.error("Ugyldig brukerhistorienummer. Gyldige verdier er 1 til 7.")
            return

        brukerhistorie = self.brukerhistorier[historienummer]
        brukerhistorie.full_brukerhistorie()
