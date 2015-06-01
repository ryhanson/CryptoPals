class XORLord:
    def __init__(self, plain, encrypted=""):
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

ice_key = "ICE"

print "Encrypting/Decrypting each line: "

lyric_lines = ["Burning 'em, if you ain't quick and nimble", "I go crazy when I hear a cymbal"]

for line in lyric_lines:
    encrypt_lord = XORLord(line)
    print "Original: " + encrypt_lord.plain
    print "Encrypted: " + encrypt_lord.encrypt_with_key(ice_key, return_hex=True)
    print "Decrypted: " + encrypt_lord.decrypt_with_key(ice_key)

print "Encrypting/Decrypting combined lyrics: "

full_lyrics = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
full_xor = XORLord(full_lyrics)

print "Original:\n" + full_lyrics
print "Encrypted:\n" + full_xor.encrypt_with_key(ice_key, return_hex=True)
print "Decrypted:\n" + full_xor.decrypt_with_key(ice_key)
