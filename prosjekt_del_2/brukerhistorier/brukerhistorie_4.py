import sqlite3
from .brukerhistorie import Brukerhistorie


class Brukerhistorie4(Brukerhistorie):
    def hent_forestillinger(self):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            query = """
           SELECT Teaterstykke.Stykketittel, Fremvisning.Fremvisningstidspunkt, COUNT(Billett.BillettID) as AntallSolgteBilletter
           FROM Fremvisning
            JOIN Teaterstykke ON Fremvisning.StykkeID = Teaterstykke.StykkeID
            LEFT JOIN Billett ON Fremvisning.Fremvisningstidspunkt = Billett.Fremvisningstidspunkt AND Fremvisning.StykkeID = Billett.StykkeID AND Fremvisning.Salnavn = Billett.Salnavn AND Fremvisning.TeaterID = Billett.TeaterID
            GROUP BY Fremvisning.Fremvisningstidspunkt, Teaterstykke.Stykketittel
            ORDER BY Fremvisning.Fremvisningstidspunkt, Teaterstykke.Stykketittel
            """
            cursor.execute(query)
            row = cursor.fetchall()
            print("Dato og stykketittel på forestillinger")
            for fremvisning in row:
                print(fremvisning)

    def full_brukerhistorie(self):
        self.hent_forestillinger()


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie4(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
