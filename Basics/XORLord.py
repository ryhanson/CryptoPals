class XORLord:
    def __init__(self, plain="", encrypted=""):
        self.plain = plain
        self.encrypted = encrypted

    def encrypt_with_key(self, key, return_hex=False):
        encrypted = ""

        for x in range(0, len(self.plain), len(key)):
            chunk = self.plain[x:x+len(key)]
            for y, z in zip(chunk, key):
                encrypted += (chr(ord(y) ^ ord(z)))

        self.encrypted = encrypted

        return self.encrypted.encode("hex") if return_hex else self.encrypted

    def decrypt_with_key(self, key):
        decrypted = ""

        for x in range(0, len(self.encrypted), len(key)):
            chunk = self.encrypted[x:x+len(key)]
            for y, z in zip(chunk, key):
                decrypted += (chr(ord(y) ^ ord(z)))

        self.plain = decrypted

        return self.plain
