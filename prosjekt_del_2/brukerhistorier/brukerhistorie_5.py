import sqlite3


class Brukerhistorie5:
    def __init__(self, teater_id, db_file_path):
        self._teater_id = teater_id
        self._db_file_path = db_file_path

    def hent_skuespillere(self):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            query = """
                SELECT Ansatt.Fornavn, Ansatt.Etternavn, Teaterstykke.Stykketittel, Rolle.Oppgavenavn 
                FROM Ansatt
                JOIN HarOppgaver ON Ansatt.AnsattID = HarOppgaver.AnsattID 
                JOIN Rolle ON HarOppgaver.OppgaveID = Rolle.OppgaveID AND HarOppgaver.StykkeID = Rolle.StykkeID 
                JOIN Teaterstykke ON Rolle.StykkeID = Teaterstykke.StykkeID
            """
            cursor.execute(query)
            row = cursor.fetchall()
            print("Navn på skuespillere og roller som opptrer i teaterstykkene:", row)

    def full_brukerhistorie(self):
        self.hent_skuespillere()


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie5(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
