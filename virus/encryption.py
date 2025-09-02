class Encryptor:
    def __init__(self, key: str, data):
        self.key = key
        self.data = str(data).encode("utf-8")
        self.key_length = len(self.key)
        self.data_length = len(self.data)

    def encrypt(self) -> bytes:
        encrypted_bytes = bytes([self.data[i] ^ ord(self.key[i % self.key_length]) for i in range(self.data_length)])
        print(f"Encrypted bytes: {encrypted_bytes}")
        return encrypted_bytes