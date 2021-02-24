from configparser import ConfigParser

class Properties:

    def __init__(self):

        self.config = ConfigParser()
        self.config.read('resources/properties.ini')
        
        self.host = self.config.get('database','host')
        self.port = self.config.get('database','port')
        self.database = self.config.get('database','database')
        self.username = self.config.get('database','username')
        self.password = self.config.get('database','password')

        self.output_path = self.config.get('result','output_path')