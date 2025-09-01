class FileWriter:
    def __init__(self, filename: str):
        self.file = open(filename, 'a')
    def write_data(self, data: list) -> None:
        for i in data:
            self.file.write(data + '\n')

"""
receives string and writes to file
"""
