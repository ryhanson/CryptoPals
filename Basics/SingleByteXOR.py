hexed = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def find_key(hex_str):
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with',
                    'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her',
                    'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up',
                    'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time',
                    'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could',
                    'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think',
                    'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new',
                    'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']

    for k in range(0, 255):
        decrypted = decrypt(hex_str, k)

        for y in range(0, len(common_words)):
            word = " " + common_words[y] + " "
            if word in decrypted:
                print "Word found: " + common_words[y]
                print "Potential key: " + str(chr(k))
                return k

def decrypt(hex_str, key):
    return "".join(chr(int(hex_str[x:x+2], 16) ^ key) for x in range(0, len(hex_str), 2))

valid_key = find_key(hexed)
print "Using key '" + str(chr(valid_key)) + "', message: " + decrypt(hexed, valid_key)
