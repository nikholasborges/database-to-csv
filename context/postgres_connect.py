from util.config_reader import Properties
from util.log_config import LogConfig

import psycopg2

class PostgresConnect:

    def __init__(self, logObj):

        self.log = logObj
        self.properties = Properties()

        self.con = ''

    def connect(self):

        self.log.write(f'Trying to connect to {self.properties.host} in the {self.properties.database} database...')

        try:
            self.con = psycopg2.connect(host=self.properties.host, 
                                        port=self.properties.port, 
                                        database=self.properties.database, 
                                        user=self.properties.username, 
                                        password=self.properties.password)

        except(Exception, psycopg2.DatabaseError) as error:
            self.log.write('Error while trying to connect to the database.')
            self.log.write(f'ERROR: {error}')
        
        self.log.write(f'Connected sucessfully.')

        return self.con.cursor()

    def close_connection(self):

        if self.con is not None:
            self.con.close()
            self.log.write('Database connection closed.')
        else:
            self.log.write('Database connection was already closed.')