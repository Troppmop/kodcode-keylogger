import base64

class Decryptor:
    def __init__(self, content, password, is_string=True):
        """
        content: either file path (default) or encrypted string
        is_string: True if content is already encrypted string, False if file path
        """
        self.content = content
        self.password = password
        self.is_string = is_string

    def read_content(self):
        if self.is_string:
            # content is already the base64 string
            return base64.b64decode(self.content)
        else:
            # content is a file path
            with open(self.content, 'r') as f:
                return base64.b64decode(f.read().strip())

    def decrypt(self, contents):
        decrypted_bytes = bytearray()
        key = self.password.encode('utf-8')
        for i in range(len(contents)):
            decrypted_bytes.append(contents[i] ^ key[i % len(key)])
        return decrypted_bytes.decode('utf-8')

    def get_decrypted_string(self):
        contents = self.read_content()
        decrypted_contents = self.decrypt(contents)
        decrypted_list = decrypted_contents.strip("[]").split(", ")
        decrypted_string = ''.join([
            item.strip("\"\'\'\"\"") if item.startswith("\"\'") and item.endswith("\'\"") else item
            for item in decrypted_list
        ])
        return decrypted_string


""""
file = sys.argv[1]
password = sys.argv[2]

with open(file, 'r') as f:
    contents = f.read().strip()

contents = base64.b64decode(contents)

def decrypt(contents, password):
    decrypted_bytes = bytearray()
    key = password.encode('utf-8')
    for i in range(len(contents)):
        decrypted_bytes.append(contents[i] ^ key[i % len(key)])
    return decrypted_bytes.decode('utf-8')

decrypted_contents = decrypt(contents, password)
decrypted_list = decrypted_contents.strip("[]").split(", ")

#   filter(lambda x = decrypted_list: x != example, " ")
#print(decrypted_list[0].strip("\"\'\'\"\""))


decrypted_string = ''.join([item.strip("\"\'\'\"\"") if item.startswith("\"\'") and item.endswith("\'\"") else item for item in decrypted_list])
print(decrypted_string)
"""