import logging

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt='[%X]',
    handlers=[RichHandler()],
)

__version__ = '0.1.0'
