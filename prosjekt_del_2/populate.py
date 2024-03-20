import sqlite3
import sys


def command_handler(commands={}):
    def decorator(func):
        commands[func.__name__] = func

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    decorator.commands = commands
    return decorator


cmd_handler = command_handler()


class Populater:
    @staticmethod
    def execute_command(command, *args):
        if command in cmd_handler.commands:
            cmd_handler.commands[command](populate, *args)
        else:
            print(f"No command found for: {command}")

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
                        [int(seat) for seat in line.strip().replace("x", "")])
        return områder, dato

    def _les_sqlite_db(self):
        with sqlite3.connect(self._db_file_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cur.fetchall()
            db_contents = {}
            for table_name in tables:
                cur.execute(f"SELECT * FROM {table_name[0]}")
                table_data = cur.fetchall()
                column_names = [description[0]
                                for description in cur.description]
                db_contents[table_name[0]] = {
                    "columns": column_names, "rows": table_data}
        return db_contents

    @cmd_handler
    def les_db(self, tabeller):
        db_contents = self._les_sqlite_db()

        for table, data in db_contents.items():
            if table not in tabeller and tabeller:
                continue
            print(f"Table: {table}")
            print("Columns:", data["columns"])
            for row in data["rows"]:
                print(row)
            print("\n")

    @cmd_handler
    def sett_inn_stykke(self, stykketittel, varighet_minutt):
        con = sqlite3.connect(self._db_file_path)
        cursor = con.cursor()
        cursor.execute("INSERT INTO Teaterstykke (Stykketittel, VarighetMinutt) VALUES (?, ?)",
                       (stykketittel, varighet_minutt))
        con.commit()
        con.close()

    @cmd_handler
    def sett_inn_sal(self, sal_filnavn, stykke_id):
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
                        if not status:
                            continue
                        kolonnenummer = j + 1
                        cursor.execute("INSERT INTO Billett (Kolonnenummer, Radnummer, Områdenummer, Salnavn, TeaterID, Fremvisningstidspunkt, StykkeID) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                       (kolonnenummer, radnummer, områdenummer, salnavn, self._teater_id, dato, stykke_id))

    @cmd_handler
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
                        if not status:
                            continue
                        kolonnenummer = j + 1
                        cursor.execute("INSERT INTO Billett (Kolonnenummer, Radnummer, Områdenummer, Salnavn, TeaterID, Fremvisningstidspunkt, StykkeID) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                       (kolonnenummer, radnummer, områdenummer, salnavn, self._teater_id, dato, stykke_id))

    @cmd_handler
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

    @cmd_handler
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

    @cmd_handler
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

    @cmd_handler
    def hent_forestillinger():
        with sqlite3.connect("Theatre.db") as con:
            cursor = con.cursor()

            query = """
            SELECT Stykketittel, Fremvisningstidspunkt, COUNT(BillettID) as AntallSolgteBilletter
            FROM Fremvisning
            JOIN Teaterstykke on Fremvisning.StykkeID = Teaterstykke.StykkeID
            JOIN Billett on Fremvisning.FremvisningID = Billett.FremvisningID
            GROUP BY Fremvisning.FremvisningID
            """
            cursor.execute(query)
            row = cursor.fetchall()
            print("Dato og stykketittel på best solgte forestillinger", row)


TEATER_ID = 1
DB_FILE_PATH = "Theatre.db"
populate = Populater(TEATER_ID, DB_FILE_PATH)

command = sys.argv[1]
arguments = sys.argv[2:]
Populater.execute_command(command, *arguments)
