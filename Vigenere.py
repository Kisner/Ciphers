#incomplete
class Vigenere:
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def Encrypt(self):
        encryption = ''
        message = self.message
        size = len(self.message)
        key_size = len(self.key)
        key = self.key

        for i in range(size):
            key_length = len(key)
            if key_length == len(key):
                i = 0
            if key_length == size:
                break
            key += key[i]

        for i in range(size):
            if message[i].isupper():
                letter = ord(message[i])
                key_letter = ord(key[key_size])
                encryption += chr(((letter - 65) + (key_letter - 65)) % 26 + 65)
                key_size += 1
            elif message[i].islower():
                letter = ord(message[i])
                key_letter = ord(key[key_size])
                encryption += chr(((letter - 97) + (key_length - 97)) % 26 + 97)
                key_size += 1
            else:
                encryption += message[i]
            key_length = len(key)
            if key_size == key_length:
                key_size = 0

        self.message = encryption
        print(self.message)

if __name__ == '__main__':
    test = Vigenere("This is a test", 'candy')
    test.Encrypt()

