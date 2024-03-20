import sqlite3
from .brukerhistorie import Brukerhistorie

class Brukerhistorie7(Brukerhistorie):
    
    def finn_skuespillere_som_spilt_sammen(self, fornavn: str, etternavn: str):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            sql =   """
                    WITH SkuespillerOppgaver AS (
                    SELECT ho.AnsattID, d.Aktnummer, d.StykkeID
                    FROM Bruker b
                    JOIN Ansatt a ON b.BrukerID = a.BrukerID
                    JOIN HarOppgaver ho ON a.AnsattID = ho.AnsattID
                    JOIN Deltar d ON ho.OppgaveID = d.OppgaveID AND ho.StykkeID = d.StykkeID
                    WHERE b.Fornavn = ? AND b.Etternavn = ?
                    )
                    SELECT DISTINCT b.Fornavn, b.Etternavn, ts.Stykketittel
                    FROM SkuespillerOppgaver so
                    JOIN Deltar d ON so.Aktnummer = d.Aktnummer AND so.StykkeID = d.StykkeID
                    JOIN HarOppgaver ho ON d.OppgaveID = ho.OppgaveID AND d.StykkeID = ho.StykkeID
                    JOIN Ansatt a ON ho.AnsattID = a.AnsattID
                    JOIN Bruker b ON a.BrukerID = b.BrukerID
                    JOIN Teaterstykke ts ON so.StykkeID = ts.StykkeID
                    WHERE NOT (a.AnsattID IN (SELECT AnsattID FROM SkuespillerOppgaver))
                    ORDER BY ts.Stykketittel, b.Etternavn, b.Fornavn
                    """
        cursor.execute(sql, (fornavn, etternavn))
        resultater = cursor.fetchall()

        if resultater:
            print(f"Skuespillere som har spilt sammen med {fornavn} {etternavn}:\n")
            current_stykke = ""
            for resultat in resultater:
                if resultat[2] != current_stykke:
                    if current_stykke != "":
                        print("\n")
                    current_stykke = resultat[2]
                    print(f"'{current_stykke}':")
                print(f"  - {resultat[0]} {resultat[1]}")
        else:
            print(f"Ingen resultater funnet for skuespilleren {fornavn} {etternavn}.")

        con.close()



    def full_brukerhistorie(self):
        fornavn = input("Fornavn:")
        etternavn= input("Etternavn:")
        self.finn_skuespillere_som_spilt_sammen(fornavn, etternavn)



if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie7(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
