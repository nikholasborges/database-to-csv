import logging
from sys import stdout
from datetime import date

class LogConfig():

    def __init__(self):
        
        self.logger = logging.getLogger('extraction_application')
        self.file_handler = None
        self.console_handler = None
        self.level = logging.INFO

        self.setLogConfig()

    def setLogConfig(self):

        date_now = date.today().strftime('%d%m%Y')

        file_path = f'log/extraction_application_{date_now}.log'

        self.file_handler = logging.FileHandler(file_path, encoding='utf-8', delay=True)
        self.file_handler.setLevel(self.level)

        # create console handler with a higher log level
        self.console_handler = logging.StreamHandler(stdout)
        self.console_handler.setLevel(self.level)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        self.file_handler.setFormatter(formatter)
        self.console_handler.setFormatter(formatter)

        self.logger.setLevel(self.level)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)
    
    def write(self, message):
        self.logger.info(message)

    