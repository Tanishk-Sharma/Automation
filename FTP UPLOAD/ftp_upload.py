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
        """ Connects to FTP using credentials given. Max 10 tries. Returns connections status - T/F """
        connected = False
        connection_count = 0
        while not connected:
            try:
                if connection_count == 10:
                    break
                self.ftp_session = ftplib.FTP(self.HOST, self.USER, self.PASS)
                connected = True
            except:
                self.logger.warning('Unable to connect to FTP Host. [ ' + str(connection_count) + ' ]')
                connection_count += 1
        if not connected:
            self.logger.error('Terminating after [ 10 ] unsuccessful attempts to login...')
            return connected
        self.logger.info('Connected to FTP successfully')
        return connected

    def upload_to_FTP(self):
        """ Uploads the zip file to FTP """
        self.logger.info('Beginning upload to FTP')
        self.zipfile_name = self.zipfile_path.split('\\')[-1]
        # self.zipfile_object = open(self.zipfile_path, 'rb')
        with open(self.zipfile_path, 'rb') as self.zipfile_object:
            try:
                self.logger.info('Opened file: ' + self.zipfile_path)
                self.ftp_session.storbinary('STOR ' + self.zipfile_name, self.zipfile_object)
                self.logger.info('SUCCESS: ' + self.zipfile_name)

            except Exception:
                self.logger.error('ERROR', exc_info=True)

    def close_connection_to_FTP(self):
        self.logger.info('Closing FTP Connection')
        self.ftp_session.quit()
        self.logger.info('FTP Connection closed')
        
# Absolute path only
zipfile_path = input('Zip file path: ')
host = input('FTP Host: ')
user = input('FTP User: ')
pwd = input('FTP Password: ')
ftpupload = FTPUpload(host, user, pwd, zipfile_path)
ftpupload.connect_to_FTP()
ftpupload.upload_to_FTP()
ftpupload.close_connection_to_FTP()
print('Done')

