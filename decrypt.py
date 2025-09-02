import sys
import base64

if len(sys.argv) != 3:
    print("Usage: python decrypt.py <file> <password>")
    sys.exit(1)

file = sys.argv[1]
password = sys.argv[2]

# Read the file in binary mode
with open(file, 'r') as f:
    contents = f.read().strip()

contents = base64.b64decode(contents)

def decrypt(contents, password):
    decrypted_bytes = bytearray()
    key = password.encode('utf-8')
    for i in range(len(contents)):
        decrypted_bytes.append(contents[i] ^ key[i % len(key)])
    return decrypted_bytes.decode('utf-8')

decrypted_contents = decrypt(contents, password).strip('[]').split(', ')
decrypted_contents = ''.join([chr(int(i)) for i in decrypted_contents])

sys.stdout.write(decrypted_contents)

