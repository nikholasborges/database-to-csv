import os
from util.log_config import LogConfig
from util.file_reader import FileReader
from util.csv_writer import CSVWriter
from util.config_reader import Properties
from context.postgres_connect import PostgresConnect
from context.postgres_query_handler import QueryHandler


def main():
    
    log = LogConfig()
    file_reader = FileReader()
    database = PostgresConnect(log)
    query_handler = QueryHandler(log)
    querys = {}

    log.write('*'*10 + ' APPLICATION START ' + '*'*10)
    
    log.write('Loading querys to generate...')

    files = os.listdir('./query')

    if files:

        for file in files:

            if file.endswith(".sql"):
                log.write(f'file found: {file}')

                querys[os.path.join('.\\query', file)] = file

        for key in querys:
            
            file_path = key
            query_name = querys[key]

            current_query = file_reader.read_text_file(file_path)

            try:
                database_cursor = database.connect()

                log.write(f'executing query: {query_name} ')
                log.write(f'statement: {current_query}')

                result_set = query_handler.execute_query(database_cursor, current_query)

                writer = CSVWriter(result_set, query_name, log)

                log.write('Writing result...')

                writer.write_csv()

                # log.write(result_set['content'])

            except(Exception) as error:
                log.write(f'Error while trying to execute query.')
                log.write(f'ERROR: {error}')
            
            finally:
                database_cursor.close()
                database.close_connection()
        else:
            log.write('No queries found to generate.')


    log.write('*'*10 + ' APPLICATION END ' + '*'*10)

if __name__ == "__main__":
    main()