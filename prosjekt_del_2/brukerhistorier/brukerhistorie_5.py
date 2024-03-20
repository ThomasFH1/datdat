import sqlite3
from .brukerhistorie import Brukerhistorie


class Brukerhistorie5(Brukerhistorie):
    def hent_skuespillere(self):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            query = """
                SELECT Teaterstykke.Stykketittel, Bruker.Fornavn || ' ' || Bruker.Etternavn AS Fullt_navn, Rolle.Oppgavenavn
                FROM Bruker
                JOIN Ansatt ON Ansatt.BrukerID = Bruker.BrukerID
                JOIN HarOppgaver ON Ansatt.AnsattID = HarOppgaver.AnsattID
                JOIN Rolle ON HarOppgaver.OppgaveID = Rolle.OppgaveID AND HarOppgaver.StykkeID = Rolle.StykkeID
                JOIN Teaterstykke ON Rolle.StykkeID = Teaterstykke.StykkeID;
            """
            cursor.execute(query)
            row = cursor.fetchall()
            print("Navn på skuespillere og roller som opptrer i teaterstykkene:")
            for skuespiller in row:
                print(skuespiller)

    def full_brukerhistorie(self):
        self.hent_skuespillere()


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie5(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
