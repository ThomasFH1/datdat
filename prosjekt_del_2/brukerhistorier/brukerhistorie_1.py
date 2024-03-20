import sqlite3
from .brukerhistorie import Brukerhistorie
from ..miscellaneous.les_salfil import les_salfil


class Brukerhistorie1(Brukerhistorie):
    def sett_inn_stoler(self, sal_filnavn):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()
            områder, dato = les_salfil(f"{sal_filnavn}.txt")
            salnavn = " ".join([word.capitalize()
                                for word in sal_filnavn.split("-")])

            områdenummer = 0
            for områdenavn, rader in områder.items():
                områdenummer += 1
                cursor.execute(
                    "INSERT INTO Område VALUES (?, ?, ?, ?)",
                    (områdenummer, områdenavn, salnavn, self._teater_id)
                )
                for i, rad in enumerate(reversed(rader)):
                    radnummer = i + 1
                    cursor.execute(
                        "INSERT INTO Rad VALUES (?, ?, ?, ?)",
                        (radnummer, områdenummer,
                         salnavn, self._teater_id)
                    )
                    for j, status in enumerate(rad):
                        kolonnenummer = j + 1
                        "INSERT INTO Stol VALUES (?, ?, ?, ?, ?)",
                        (kolonnenummer, radnummer, områdenavn,
                         salnavn, self._teater_id)
            con.commit()
    def full_brukerhistorie(self):
        self.sett_inn_stoler("hovedscenen")
        self.sett_inn_stoler("gamle-scene")


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie1(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
