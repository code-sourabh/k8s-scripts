import logging
from decouple import config

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(level=config('LOGGING_LEVEL', default=20, cast=int))