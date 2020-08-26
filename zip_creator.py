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
      """ Zipping is performed here """
        try:
            self.logger.info('Zipping Files')
            self.logger.debug('Source path format expected: folder\\filename.extension')
            self.logger.debug('Destination path format expected: folder\\filename.zip')
            self.logger.debug('Given Source path: ' + self.source_path)
            self.logger.debug('Given Destination path: ' + self.destination_path)

            ### Separating the source, destination paths into parameters for zip operations (shutil) ###
            base_path = os.path.basename(self.destination_path)
            self.logger.debug('base_path: ' + base_path)

            name_of_zip_file = base_path.split('.')[0]
            self.logger.debug('name_of_zip_file: ' + name_of_zip_file)

            extension = base_path.split('.')[1]
            self.logger.debug('extension: ' + extension)

            zip_source = os.path.dirname(self.source_path)
            self.logger.debug('zip_source: ' + zip_source)

            zip_destination = os.path.basename(self.source_path.strip(os.sep))
            self.logger.debug('zip_destination: ' + zip_destination)

            shutil.make_archive(name_of_zip_file, extension, zip_source, zip_destination)
            shutil.move('%s.%s' % (name_of_zip_file, extension), self.destination_path)

            self.logger.info('SUCCESS: ' + base_path)

        except Exception:
            # exc_info=True will let us log the full error stack
            self.logger.exception('ERROR', exc_info=True)


print('Absolute path only')
source = input('Source path: ')
destination = input('Destination path: ')

zipcreator = ZipCreator(source, destination)
zipcreator.create_zip()

