import sys
from miscellaneous import CommandManager


TEATER_ID = 1
DB_FILE_PATH = "Theatre.db"
cmd_manager_instance = CommandManager(TEATER_ID, DB_FILE_PATH)

command = sys.argv[1]
arguments = sys.argv[2:]
cmd_manager_instance.execute_command(command, *arguments)
