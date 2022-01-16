import logging
from colorama import Fore, Back, Style


logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(message)s')
logger = logging.getLogger(__name__)


def info(msg):
    logger.info(Fore.GREEN + msg)


def error(msg):
    logger.info(Fore.RED + msg)


def debug(msg):
    logger.debug(Fore.BLUE + msg)


def warning(msg):
    logger.warning(Fore.YELLOW + msg)


