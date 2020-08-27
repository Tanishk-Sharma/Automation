import ftplib
import logging
from datetime import datetime


class FTPUpload:
    
    def __init__(self, host, user, pwd, zipfile_path):
        """ Initialize the parameters to be used: Logging, FTP credentials, File to upload """
        # Logging parameters:
        date_suffix = datetime.today().strftime('%d%m%Y')
        LOG_FILENAME = 'logs\\ftp_upload_' + date_suffix + '.log'
        LOG_FORMAT = "[%(asctime)s] - [ %(levelname)s ]  | %(funcName)s | %(message)s"
        LOG_LEVEL = logging.DEBUG
        logging.basicConfig(filename=LOG_FILENAME,
                            level=LOG_LEVEL,
                            format=LOG_FORMAT)
        # Get a Root Logger Object with above config
        self.logger = logging.getLogger()
        self.logger.info('--NEW RUN--')

        # Initialize FTP login credentials
        self.HOST = host
        self.USER = user
        self.PASS = pwd
        self.logger.info('FTP credentials initialized')

        # Initialize the zipfile path to upload to FTP
        self.zipfile_path = zipfile_path
        self.logger.info('Given zipfile path: ' + self.zipfile_path)

    def connect_to_FTP(self):
        pass

    def upload_to_FTP(self):
        pass

    def close_connection_to_FTP(self):
        pass

