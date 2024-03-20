import sqlite3


class Brukerhistorie2:
    @staticmethod
    def _les_sal(salfil):
        områder = {}
        with open(salfil, "r") as f:
            dato = f.readline().strip()

            for line in f:
                if not line[0].isdigit():
                    last_område = line.strip()
                    områder[last_område] = []
                else:
                    ny_rad = [int(seat)
                              for seat in line.strip().replace("x", "")]
                    områder[last_område].append(ny_rad)
        return områder, dato

    def __init__(self, teater_id, db_file_path):
        self._teater_id = teater_id
        self._db_file_path = db_file_path

    def _sett_inn_billett(self, kolonnenummer, radnummer, områdenummer, salnavn, dato, stykke_id):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()
            cursor.execute(
                """INSERT INTO Billett 
                (Kolonnenummer, Radnummer, Områdenummer, Salnavn, TeaterID, Fremvisningstidspunkt, StykkeID) 
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (kolonnenummer, radnummer, områdenummer, salnavn, self._teater_id, dato, stykke_id))
            con.commit()

    def _sett_inn_fremvisning(self, salnavn, stykke_id, dato):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            cursor.execute(
                "INSERT INTO Fremvisning VALUES (?, ?, ?, ?)",
                (dato, salnavn, self._teater_id, stykke_id)
            )
            con.commit()

    def sett_inn_billetter_til_fremvisning(self, sal_filnavn, stykke_id):
        områder, dato = self._les_sal(f"{sal_filnavn}.txt")
        salnavn = " ".join([word.capitalize()
                            for word in sal_filnavn.split("-")])

        self._sett_inn_fremvisning(salnavn, stykke_id, dato)

        områdenummer = 0
        for områdenavn, rader in områder.items():
            områdenummer += 1
            for i, rad in enumerate(reversed(rader)):
                radnummer = i + 1
                for j, status in enumerate(rad):
                    if not status:
                        continue
                    kolonnenummer = j + 1
                    self._sett_inn_billett(
                        kolonnenummer, radnummer, områdenummer, salnavn, dato, stykke_id)

    def full_brukerhistorie(self):
        self.sett_inn_billetter_til_fremvisning("hovedscenen", 2)
        self.sett_inn_billetter_til_fremvisning("gamle-scenen", 1)


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie2(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
