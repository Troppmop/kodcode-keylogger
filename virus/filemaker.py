class FileWriter:
    def __init__(self, filename: str):
        self.file = open(filename, 'w')
    def write_data(self, data: list) -> None:
        contents = ""
        for i in data:
            contents += str(i) + "\n"
        self.file.write(contents)

"""
receives string and writes to file
"""
