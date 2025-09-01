import sys

file = sys.argv[1]
password = sys.argv[2]
contents = open(file,'r')

def decrypt(logs, key):
    pass

decrypted_contents = decrypt(contents, password)

sys.stdout.write(decrypted_contents)

"""
decrypts the encrypted keylog file
"""
