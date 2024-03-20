from ..brukerhistorier import BrukerhistorieHandler
from .db_utils import DBUtils


def command_handler(commands={}):
    def decorator(func):
        commands[func.__name__] = func

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    decorator.commands = commands
    return decorator


cmd = command_handler()


class CommandManager(BrukerhistorieHandler):
    def __init__(self, teater_id, db_file_path):
        self._teater_id = teater_id
        self._db_file_path = db_file_path

        self._brukerhistorie_handler_instance = BrukerhistorieHandler(
            self._teater_id, self._db_file_path)

    def execute_command(self, command, *args):
        if command in cmd.commands:
            cmd.commands[command](self, *args)
        else:
            print(f"No command found for: {command}")

    @cmd
    def les_db(self, *tabeller):
        db_utils_instance = DBUtils(self._db_file_path)
        db_utils_instance.les_db(tabeller)

    @cmd
    def load_initial_data(self):
        db_utils_instance = DBUtils(self._db_file_path)
        db_utils_instance.load_intial_data()

    @cmd
    def brukerhistorier(self, brukerhistorienummer):
        self._brukerhistorie_handler_instance.brukerhistorier(
            brukerhistorienummer)

    #  ↓ Alle metoder som brukes innad i brukerhistoriene dersom bruker ønsker å kjøre dem selv
    #  ↓ Trengs strengt tatt ikke til oppgaven

    @cmd
    def sett_inn_billetter_til_fremvisning(self, sal_filnavn, stykke_id):
        brukerhistorie = self._brukerhistorie_handler_instance.brukerhistorier[2]
        brukerhistorie.sett_inn_billetter_til_fremvisning(
            sal_filnavn, stykke_id)

    @cmd
    def hent_ledige_rader(self, mengde, fremvisningstidspunkt, salnavn, stykke_id):
        brukerhistorie = self._brukerhistorie_handler_instance.brukerhistorier[3]
        brukerhistorie.hent_ledige_rader(
            mengde, fremvisningstidspunkt, salnavn, stykke_id)

    @cmd
    def utfør_kjøp(self, stoler, fremvisningstidspunkt, salnavn, stykke_id):
        brukerhistorie = self._brukerhistorie_handler_instance.brukerhistorier[3]
        brukerhistorie.utfør_kjøp(
            stoler, fremvisningstidspunkt, salnavn, stykke_id)

    @cmd
    def hent_forestillinger(self):
        brukerhistorie = self._brukerhistorie_handler_instance.brukerhistorier[4]
        brukerhistorie.hent_forestillinger()

    @cmd
    def hent_skuespillere(self):
        brukerhistorie = self._brukerhistorie_handler_instance.brukerhistorier[5]
        brukerhistorie.hent_skuespillere()

    @cmd
    def best_solgte_forestillinger(self):
        brukerhistorie = self._brukerhistorie_handler_instance.brukerhistorier[6]
        brukerhistorie.best_solgte_forestillinger()
