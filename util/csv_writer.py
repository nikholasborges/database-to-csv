import csv
from .config_reader import Properties

class CSVWriter:

    def __init__(self, data_set, query_name, log):
        
        self.query_name = query_name.split('.')[0] + '.csv'
        self.header = data_set['header']
        self.data = data_set['content']

        self.properties = Properties()

        self.log = log

    def write_csv(self):

        full_file_path = self.properties.output_path + self.query_name
        
        with open(full_file_path, mode='w') as result_file:
            csv_writer = csv.writer(result_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')

            csv_writer.writerow(self.header)

            for row in self.data:
                csv_writer.writerow(row)

        self.log.write(f'Writed sucessfully. result saved in: {full_file_path}')
