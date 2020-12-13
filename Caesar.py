class Caesar:
    def __init__(self, message, shift):
        self.message = message
        self.shift = shift

    def encrypt(self):
        encryption = ''
        message = self.message
        size = len(self.message)
        for i in range(size):
            if message[i].isupper():
                letter = ord(message[i])
                encryption += chr((letter + self.shift - 65) % 26 + 65)
            elif message[i].islower():
                letter = ord(message[i])
                encryption += chr((letter + self.shift - 97) % 26 + 97)
            else:
                encryption += message[i]
        self.message = encryption

    def decrypt(self):
        decrypt = ''
        message = self.message
        size = len(self.message)
        for i in range(size):
            if message[i].isupper():
                letter = ord(message[i])
                decrypt += chr((letter + 26 - (self.shift % 26) - 65) % 26 + 65)
            elif message[i].islower():
                letter = ord(message[i])
                decrypt += chr((letter + 26 - (self.shift % 26) - 97) % 26 + 97)
            else:
                decrypt += message[i]
        self.message = decrypt
        print(self.message)


if __name__ == '__main__':
    test = Caesar("This is a test", 4)
    test.encrypt()
    test.decrypt()


