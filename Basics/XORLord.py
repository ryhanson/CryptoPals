class XORLord:
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with',
                    'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her',
                    'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up',
                    'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time',
                    'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could',
                    'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think',
                    'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new',
                    'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']

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
                print(str(y) + " ^ " + str(z))
                decrypted += (chr(ord(y) ^ ord(chr(z))))

        self.plain = decrypted

        return self.plain

    def find_words(self, plain):
        words_found = []

        for y in range(0, len(self.common_words)):
            word = " " + self.common_words[y] + " "

            if word in plain:
                words_found.append(self.common_words[y])

        return words_found
