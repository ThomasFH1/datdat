import sqlite3
import sys
from .brukerhistorier import *


def command_handler(commands={}):
    def decorator(func):
        commands[func.__name__] = func

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    decorator.commands = commands
    return decorator


cmd_handler = command_handler()


class CommandManager:
    @staticmethod
    def execute_command(command, *args):
        if command in cmd_handler.commands:
            cmd_handler.commands[command](populate, *args)
        else:
            print(f"No command found for: {command}")

    def __init__(self, teater_id, db_file_path):
        self._teater_id = teater_id
        self._db_file_path = db_file_path

        self.brukerhistorie_2_instance = Brukerhistorie2(
            teater_id, db_file_path)
        self.brukerhistorie_3_instance = Brukerhistorie3(
            teater_id, db_file_path)
        self.brukerhistorie_4_instance = Brukerhistorie4(
            teater_id, db_file_path)
        self.brukerhistorie_5_instance = Brukerhistorie5(
            teater_id, db_file_path)
        self.brukerhistorie_6_instance = Brukerhistorie6(
            teater_id, db_file_path)

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
    def les_db(self, *tabeller):
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
    def sett_inn_sal(self, sal_filnavn, stykke_id):
        # TODO
        pass

    @cmd_handler
    def sett_inn_billetter_til_fremvisning(self, sal_filnavn, stykke_id):
        self.brukerhistorie_2_instance.sett_inn_billetter_til_fremvisning(
            sal_filnavn, stykke_id)

    @cmd_handler
    def hent_skuespillere(self):
        self.brukerhistorie_5_instance.hent_skuespillere()

    @cmd_handler
    def best_solgte_forestillinger(self):
        self.brukerhistorie_6_instance.best_solgte_forestillinger()

    @cmd_handler
    def hent_forestillinger(self):
        self.brukerhistorie_4_instance.hent_forestillinger

    @cmd_handler
    def brukerhistorie(self, historienummer):
        try:
            historienummer = int(historienummer)
        except:
            raise Exception("Brukerhistorienummer må være et heltall")
        if 1 <= historienummer <= 7:
            raise Exception("Brukerhistorienummer må være fra 1 til og med 7")

        if historienummer == 1:
            pass
        elif historienummer == 2:
            self.brukerhistorie_2_instance.full_brukerhistorie()
        elif historienummer == 3:
            self.brukerhistorie_3_instance.full_brukerhistorie()
        elif historienummer == 4:
            self.brukerhistorie_4_instance.full_brukerhistorie()
        elif historienummer == 5:
            self.brukerhistorie_5_instance.full_brukerhistorie()
        elif historienummer == 6:
            self.brukerhistorie_6_instance.full_brukerhistorie()
        elif historienummer == 7:
            pass


TEATER_ID = 1
DB_FILE_PATH = "Theatre.db"
populate = CommandManager(TEATER_ID, DB_FILE_PATH)

command = sys.argv[1]
arguments = sys.argv[2:]
CommandManager.execute_command(command, *arguments)
