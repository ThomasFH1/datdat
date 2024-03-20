import sqlite3
from .brukerhistorie import Brukerhistorie

class Brukerhistorie6(Brukerhistorie):
    def best_solgte_forestillinger(self):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            query = """
            SELECT Stykketittel, Fremvisningstidspunkt, COUNT(BillettID) as AntallSolgteBilletter
            FROM Fremvisning
            JOIN Teaterstykke on Fremvisning.StykkeID = Teaterstykke.StykkeID
            JOIN Billett on Fremvisning.FremvisningID = Billett.FremvisningID
            GROUP BY Fremvisning.FremvisningID
            ORDER BY AntallSolgteBilletter DESC
            """
            cursor.execute(query)
            row = cursor.fetchall()
            print(
                "Dato og stykketittel på best solgte forestillinger, sortert i synkende rekkefølge:", row)

    def full_brukerhistorie(self):
        self.best_solgte_forestillinger


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie6(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
