import sqlite3
import sys


class Populate:
    def __init__(self, teater_id, db_file_path):
        self._teater_id = teater_id
        self._db_file_path = db_file_path

    def _les_sal(self, salfil):
        områder = {}
        with open(salfil, "r") as f:
            dato = f.readline().strip()

            for line in f:
                if not line[0].isdigit():
                    last_område = line.strip()
                    områder[last_område] = []
                else:
                    områder[last_område].append(
                        [seat for seat in line.strip().replace("x", "")])
        return områder, dato

    def sett_inn_stykke(self, stykketittel, varighet_minutt):
        con = sqlite3.connect(self._db_file_path)
        cursor = con.cursor()
        cursor.execute("INSERT INTO Teaterstykke (Stykketittel, VarighetMinutt) VALUES (?, ?)",
                       (stykketittel, varighet_minutt))
        con.commit()
        con.close()

    def sett_inn_fremvisning(self, sal_filnavn, stykke_id):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()
            områder, dato = self._les_sal(f"{sal_filnavn}.txt")
            salnavn = " ".join([word.capitalize()
                                for word in sal_filnavn.split("-")])
            cursor.execute("INSERT INTO Fremvisning VALUES (?, ?, ?, ?)",
                           (dato, salnavn, self._teater_id, stykke_id))
            områdenummer = 0
            for områdenavn, rader in områder.items():
                områdenummer += 1
                for i, rad in enumerate(reversed(rader)):
                    radnummer = i + 1
                    for j, status in enumerate(rad):
                        kolonnenummer = j + 1
                        if status == "1":
                            cursor.execute("INSERT INTO Billett (Kolonnenummer, Radnummer, Områdenummer, Salnavn, TeaterID, Fremvisningstidspunkt, StykkeID) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                           (kolonnenummer, radnummer, områdenummer, salnavn, self._teater_id, dato, stykke_id))

    def kjøp_seter_samme_rad(self, mengde, fremvisningstidspunkt, salnavn, stykke_id):
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
            # print(ledige_rader)
            try:
                rad = ledige_rader[0]
                for kolonne in rad["ledige_kolonner"][:int(mengde)]:
                    insert_query = """
                    INSERT INTO Billett (Kolonnenummer, Radnummer, Områdenummer, Salnavn, TeaterID, Fremvisningstidspunkt, StykkeID)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """
                    cursor.execute(
                        insert_query, (kolonne, rad["radnummer"], rad["områdenummer", salnavn, self._teater_id, fremvisningstidspunkt, stykke_id]))
                con.commit()
            except IndexError:
                raise Exception(
                    f"Ingen rader med mer enn {mengde} ledige seter!")

    def hent_skuespillere():
        with sqlite3.connect("Theatre.db") as con:
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

    def best_solgte_forestillinger():
        with sqlite3.connect("Theatre.db") as con:
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


TEATER_ID = 1
DB_FILE_PATH = "Theatre.db"
populate = Populate(TEATER_ID, DB_FILE_PATH)
if sys.argv[1] == "sett_inn_stykke":
    populate.sett_inn_stykke(sys.argv[2], sys.argv[3])
if sys.argv[1] == "sett_inn_fremvisning":
    populate.sett_inn_fremvisning(sys.argv[2], sys.argv[3])

if sys.argv[1] == "kjøp_seter_samme_rad":
    populate.kjøp_seter_samme_rad(
        sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

if sys.argv[1] == "hent_skuespillere":
    populate.hent_skuespillere()
if sys.argv[1] == "best_solgte_forestillinger":
    populate.best_solgte_forestillinger()
