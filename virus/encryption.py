class Encryptor:
    def __init__(self, key: str, data):
        self.key = key
        # convert to bytes if it's a string
        if isinstance(data, str):
            self.data = data.encode("utf-8")
        else:
            self.data = data
        self.key_length = len(self.key)
        self.data_length = len(self.data)

    def encrypt(self) -> bytes:
        return bytes([self.data[i] ^ ord(self.key[i % self.key_length]) for i in range(self.data_length)])
        #return --- IGNORE ---