import sys

if len(sys.argv) != 3:
    print("Usage: python decrypt.py <file> <password>")
    sys.exit(1)

file = sys.argv[1]
password = sys.argv[2]

# Read the file in binary mode
with open(file, 'rb') as f:
    contents = f.read()

def decrypt(data: bytes, key: str) -> bytes:
    key_length = len(key)
    return bytes([data[i] ^ ord(key[i % key_length]) for i in range(len(data))])

decrypted_contents = decrypt(contents, password)

sys.stdout.write(decrypted_contents.decode('utf-8'))

"""
decrypts the encrypted keylog file
"""
