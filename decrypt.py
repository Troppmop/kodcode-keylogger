import sys

file = sys.argv[1]
password = sys.argv[2]
contents = open(file,'r')

def decrypt(logs, key):

    output = bytearray(len(logs))
    key_length = len(key)
    for i in range(len(logs)):
        output.append(logs[i] ^ key[i % key_length])
    return output

decrypted_contents = decrypt(contents, password)

sys.stdout.write(decrypted_contents)

"""
decrypts the encrypted keylog file
"""
