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


cmd_handler = command_handler()


class CommandManager(BrukerhistorieHandler):
    def execute_command(self, command, *args):
        if command in cmd_handler.commands:
            cmd_handler.commands[command](self, *args)
        else:
            print(f"No command found for: {command}")

    def __init__(self, teater_id, db_file_path):
        self._teater_id = teater_id
        self._db_file_path = db_file_path

        self._brukerhistorie_handler_instance = BrukerhistorieHandler(
            self._teater_id, self._db_file_path)

    @cmd_handler
    def les_db(self, *tabeller):
        db_utils_instance = DBUtils(self._db_file_path)
        db_utils_instance.les_db(tabeller)

    @cmd_handler
    def brukerhistorie(self, brukerhistorienummer):
        self._brukerhistorie_handler_instance.brukerhistorie(
            brukerhistorienummer)

    #  ↓ Alle metoder som brukes innad i brukerhistoriene dersom bruker ønsker å kjøre dem selv
    #  ↓ Trengs strengt tatt ikke til oppgaven

    @cmd_handler
    def sett_inn_billetter_til_fremvisning(self, sal_filnavn, stykke_id):
        self._brukerhistorie_handler_instance.brukerhistorie_2_instance.sett_inn_billetter_til_fremvisning(
            sal_filnavn, stykke_id)

    @cmd_handler
    def hent_ledige_rader(self, mengde, fremvisningstidspunkt, salnavn, stykke_id):
        self._brukerhistorie_handler_instance.brukerhistorie_3_instance.hent_ledige_rader(
            mengde, fremvisningstidspunkt, salnavn, stykke_id)

    @cmd_handler
    def utfør_kjøp(self, stoler, fremvisningstidspunkt, salnavn, stykke_id):
        self._brukerhistorie_handler_instance.brukerhistorie_3_instance.utfør_kjøp(
            stoler, fremvisningstidspunkt, salnavn, stykke_id)

    @cmd_handler
    def hent_forestillinger(self):
        self._brukerhistorie_handler_instance.brukerhistorie_4_instance.hent_forestillinger()

    @cmd_handler
    def hent_skuespillere(self):
        self._brukerhistorie_handler_instance.brukerhistorie_5_instance.hent_skuespillere()

    @cmd_handler
    def best_solgte_forestillinger(self):
        self._brukerhistorie_handler_instance.brukerhistorie_6_instance.best_solgte_forestillinger()
