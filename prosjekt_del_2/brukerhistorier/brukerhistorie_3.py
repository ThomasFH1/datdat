import sqlite3
from miscellaneous.logger import logger

from .brukerhistorie import Brukerhistorie


class Brukerhistorie3(Brukerhistorie):
    @staticmethod
    def _spør_bruker_om_hvilken_rad(minimum_ledige_seter, ledige_rader):
        """Tar input og verifiserer at den raden har nok ledige seter."""

        try:
            områdenummer = int(
                input("Hvilket område vil du kjøpe billetter til: "))
            if not any([
                    ledig_rad["områdenummer"] == områdenummer
                    for ledig_rad in ledige_rader]):
                logger.error(
                    f"Område hadde ikke en rad med minst {minimum_ledige_seter} ledige seter!")
                exit()

            radnummer = int(input("Hvilken rad vil du kjøpe billetter til: "))
            if not any([
                    ledig_rad["områdenummer"] == områdenummer
                    and ledig_rad["radnummer"] == radnummer
                    for ledig_rad in ledige_rader]):
                logger.error(
                    f"Raden hadde ikke minst {minimum_ledige_seter} ledige seter!")
                exit()
        except ValueError:
            logger.error("Områdenummer og radnummer må være heltall")

        return områdenummer, radnummer

    def hent_ledige_rader(self, mengde, fremvisningstidspunkt, salnavn, stykke_id):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()

            query = """
            SELECT s.Radnummer, s.Områdenummer, 
            GROUP_CONCAT(s.Kolonnenummer) AS LedigeKolonner, COUNT(*) as LedigeSeter
            FROM Stol s
            LEFT JOIN Billett b ON s.Kolonnenummer = b.Kolonnenummer
                                AND s.Radnummer = b.Radnummer
                                AND s.Områdenummer = b.Områdenummer
                                AND s.Salnavn = b.Salnavn
                                AND s.TeaterID = b.TeaterID
                                AND b.Fremvisningstidspunkt = ?
                                AND b.TeaterID = ?
                                AND b.Salnavn = ?
                                AND b.StykkeID = ?
            WHERE b.BillettID IS NULL AND s.Salnavn = ? AND s.TeaterID = ?
            GROUP BY s.Radnummer, s.Områdenummer
            HAVING COUNT(*) >= ? ORDER BY Count(*) DESC 
            """
            cursor.execute(query, (fremvisningstidspunkt, self._teater_id,
                           salnavn, stykke_id, salnavn, self._teater_id, int(mengde)))
            ledige_rader = [{"radnummer": rad_data[0],
                             "områdenummer": rad_data[1],
                             "ledige_kolonner": [int(kolonne) for kolonne in rad_data[2].split(",")]}
                            for rad_data in cursor.fetchall()]
            print(f"Disse radene har minst {mengde} ledige seter:")
            for rad in ledige_rader:
                print(
                    f"Rad {rad['radnummer']} i område {rad['områdenummer']} har {len(rad['ledige_kolonner'])} ledige seter")
            return ledige_rader

    def utfør_kjøp(self, stoler, fremvisningstidspunkt, salnavn, stykke_id, kunde_id):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()
            cursor.execute("INSERT INTO Kjøp (KundeID, Kjøpstidspunkt) VALUES (?, Date('now'))",
                           (kunde_id, ))
            cursor.execute(
                "SELECT KjøpID FROM Kjøp ORDER BY KjøpID DESC LIMIT 1"
            )
            kjøp_id = cursor.fetchone()[0]
            cursor.executemany(
                """
                INSERT INTO Billett (Kolonnenummer, Radnummer, Områdenummer, 
                Salnavn, TeaterID, Fremvisningstidspunkt, StykkeID, PrisGruppe,
                KjøpID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [(stol["kolonnenummer"], stol["radnummer"], stol["områdenummer"],
                  salnavn, self._teater_id, fremvisningstidspunkt, stykke_id, "Ordinær", kjøp_id)
                 for stol in stoler]
            )

            con.commit()

    def kjøp_seter_samme_rad(
            self, minimum_ledige_seter, fremvisningstidspunkt,
            salnavn, stykke_id, kunde_id):

        ledige_rader = self.hent_ledige_rader(
            minimum_ledige_seter, fremvisningstidspunkt, salnavn, stykke_id)
        områdenummer, radnummer = self._spør_bruker_om_hvilken_rad(
            minimum_ledige_seter, ledige_rader)
        for rad in ledige_rader:
            if områdenummer == rad["områdenummer"] and radnummer == rad["radnummer"]:
                stoler = [{
                    "radnummer": radnummer,
                    "områdenummer": områdenummer,
                    "kolonnenummer": kolonnenummer
                } for kolonnenummer in rad["ledige_kolonner"][:minimum_ledige_seter]]
                self.utfør_kjøp(stoler, fremvisningstidspunkt,
                                salnavn, stykke_id, kunde_id)

                break

    def full_brukerhistorie(self):
        MINIMUM_LEDIGE_SETER = 9
        FREMVISNINGSTIDSPUNKT = '2024-03-19 18:30'
        SALNAVN = 'Hovedscenen'
        STYKKE_ID = 2
        KUNDE_ID = 30

        self.kjøp_seter_samme_rad(
            MINIMUM_LEDIGE_SETER, FREMVISNINGSTIDSPUNKT, SALNAVN, STYKKE_ID, KUNDE_ID)


if __name__ == "__main__":
    TEATER_ID = 1
    DB_FILE_PATH = "Theatre.db"
    brukerhistorie_instance = Brukerhistorie3(TEATER_ID, DB_FILE_PATH)
    brukerhistorie_instance.full_brukerhistorie()
