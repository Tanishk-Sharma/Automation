import os
import shutil
from datetime import datetime
import logging


class ZipCreator:
    def __init__(self, source, destination):
        """ Initializing the parameters - Source, Destination, Logging"""
        # Logging parameters:
        date_suffix = datetime.today().strftime('%d%m%Y')
        LOG_FILENAME = 'logs\\zip_creator_' + date_suffix + '.log'
        LOG_FORMAT = "[%(asctime)s] - [ %(levelname)s ]  | %(funcName)s | %(message)s"
        LOG_LEVEL = logging.DEBUG
        logging.basicConfig(filename=LOG_FILENAME,
                            level=LOG_LEVEL,
                            format=LOG_FORMAT)
        # Get a Root Logger Object with above config
        self.logger = logging.getLogger()
        self.logger.info('--NEW RUN--')

        # Source path format expected: folder\filename.extension
        self.source_path = source
        # Destination path format expected: folder\filename.zip
        self.destination_path = destination
        self.logger.info('Source/Destination Paths initialized')

    def create_zip(self):
      pass


