class FileReader:

    def __init__(self):
        pass

    def read_text_file(self, path):

        file = open(path, 'r')

        return file.read()