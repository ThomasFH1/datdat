import logging
import coloredlogs

# Create a logger object.
logger: logging.Logger = logging.getLogger('TDT4145 Prosjekt')
coloredlogs.install(level='DEBUG', logger=logger)
