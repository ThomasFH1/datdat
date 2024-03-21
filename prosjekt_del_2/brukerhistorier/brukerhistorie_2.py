import sqlite3
from .brukerhistorie import Brukerhistorie
from miscellaneous.les_salfil import les_salfil


class Brukerhistorie2(Brukerhistorie):
    def _sett_inn_fremvisning(self, salnavn, stykke_id, dato):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            cursor.execute(
                "INSERT INTO Fremvisning VALUES (?, ?, ?, ?)",
                (dato, salnavn, self._teater_id, stykke_id)
            )
            con.commit()

    def sett_inn_billetter_til_fremvisning(self, sal_filnavn, stykke_id):
        KUNDE_ID = 29

        områder, dato, salnavn = les_salfil(f"{sal_filnavn}")
        self._sett_inn_fremvisning(salnavn, stykke_id, dato)

        områdenummer = 0
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()
            cursor.execute("INSERT INTO Kjøp (KundeID, Kjøpstidspunkt) VALUES (?, Date('now'))",
                           (KUNDE_ID, ))
            cursor.execute(
                "SELECT KjøpID FROM Kjøp ORDER BY KjøpID DESC LIMIT 1"
            )
            kjøp_id = cursor.fetchone()[0]
            for områdenavn, rader in områder.items():
                områdenummer += 1
                for i, rad in enumerate(reversed(rader)):
                    radnummer = i + 1
                    for j, status in enumerate(rad):
                        if not status:
                            continue
                        kolonnenummer = j + 1
                        cursor.execute(
                            """INSERT INTO Billett 
                            (Kolonnenummer, Radnummer, Områdenummer, Salnavn,
                            TeaterID, Fremvisningstidspunkt, StykkeID, PrisGruppe,
                            KjøpID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (kolonnenummer, radnummer, områdenummer, salnavn,
                             self._teater_id, dato, stykke_id, "Ordinær", kjøp_id))
            con.commit()

    def full_brukerhistorie(self):
        self.sett_inn_billetter_til_fremvisning("hovedscenen", 2)
        self.sett_inn_billetter_til_fremvisning("gamle-scene", 1)


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie2(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
