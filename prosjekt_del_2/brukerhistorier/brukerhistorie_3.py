import sqlite3
from .brukerhistorie import Brukerhistorie


class Brukerhistorie3(Brukerhistorie):

    def hent_ledige_rader(self, mengde, fremvisningstidspunkt, salnavn, stykke_id):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            query = """
            SELECT s.Radnummer, s.Områdenummer, GROUP_CONCAT(s.Kolonnenummer) AS LedigeKolonner, COUNT(*) as LedigeSeter
            FROM Stol s
            LEFT JOIN Billett b ON s.Kolonnenummer = b.Kolonnenummer
                                AND s.Radnummer = b.Radnummer
                                AND s.Områdenummer = b.Områdenummer
                                AND s.Salnavn = b.Salnavn
                                AND s.TeaterID = b.TeaterID
                                AND b.Fremvisningstidspunkt = ?
                                AND b.Salnavn = ?
                                AND b.TeaterID = ?
                                AND b.StykkeID = ?
            WHERE b.BillettID IS NULL AND s.Salnavn = ? AND s.TeaterID = ?
            GROUP BY s.Radnummer, s.Områdenummer
            HAVING COUNT(*) >= ? ORDER BY Count(*) DESC 
            """
            cursor.execute(query, (fremvisningstidspunkt, self._teater_id,
                           salnavn, stykke_id, salnavn, self._teater_id, int(mengde)))
            ledige_rader = [{"radnummer": rad_data[0],
                             "områdenummer": rad_data[1],
                             "ledie_kolonner": [int(kolonne) for kolonne in rad_data[2].split(",")]}
                            for rad_data in cursor.fetchall()]
            return ledige_rader

    def utfør_kjøp(self, stoler, fremvisningstidspunkt, salnavn, stykke_id):
        # TODO
        insert_query = """
                        INSERT INTO Billett (Kolonnenummer, Radnummer, Områdenummer, Salnavn, TeaterID, Fremvisningstidspunkt, StykkeID)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()
            for stol in stoler:
                cursor.execute(
                    insert_query,
                    (stol["kolonnenummer"], stol["radnummer"], stol["områdenummer"],
                     salnavn, self._teater_id, fremvisningstidspunkt, stykke_id)
                )

    def full_brukerhistorie(self):
        # TODO
        pass


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie3(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
