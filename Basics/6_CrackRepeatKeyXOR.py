import base64
import collections

def hamming_dist(a, b):
    xored = bytes([x ^ y for (x, y) in zip(a, b)])

    return sum((xored[j] >> i) & 1 for i in range(8) for j in range(len(xored)))

def get_avg_hamming_dist(raw, chunk_size):
    chunks = get_chunks(raw, chunk_size)

    return sum(hamming_dist(c1, c2) / chunk_size for c1, c2 in zip(chunks, chunks[1:])) / len(chunks[1:])

def get_chunks(raw, chunk_size):
    return [raw[i:i+chunk_size] for i in range(0, len(raw), chunk_size)]

def decrypt_with_key(raw, key):
        result = ""

        for x in range(0, len(raw), len(key)):
            chunk = raw[x:x+len(key)]
            for y, z in zip(chunk, key):
                result += (chr(ord(chr(y)) ^ ord(chr(z))))

        return result

def transpose_bytes(raw, chunk_size):
    result_chunks = []
    raw_chunks = get_chunks(raw, chunk_size)

    for s in range(0, chunk_size, 1):
        transposed_chunk = bytearray()

        for ch in raw_chunks:
            if len(ch) == chunk_size:
                transposed_chunk.append(ch[s])

        result_chunks.append(transposed_chunk)

    return result_chunks

test_str1 = bytes('this is a test', 'ascii')
test_str2 = bytes('wokka wokka!!!', 'ascii')
correct_distance = 37
test_distance = hamming_dist(test_str1, test_str2)

print("[-] Validating Hamming Distance function...")
print("[-] Finding Distance Between: 'this is a test' and 'wokka wokka!!!'")
print("[+] Hamming Distance Found: " + str(test_distance))

if test_distance == correct_distance:
    print("[+] Hamming Distance function is working properly!\n")

with open('6.txt', 'r') as b64_file:
    decoded = base64.b64decode(b64_file.read())
    raw_bytes = bytes(decoded)
    best_average = 99999
    best_keysize = 0

    print("[-] Testing keysizes 2 to 40...")
    for keysize in range(2, 40):
        print("[-] Getting avearge Hamming distance for keysize: " + str(keysize))
        avg_distance = get_avg_hamming_dist(raw_bytes, keysize)
        print("[+] Average Distance for keysize " + str(keysize) + " : " + str(avg_distance))

        if avg_distance < best_average:
            best_average = avg_distance
            best_keysize = keysize

    print('[+] Keysize of ' + str(keysize) + ' had the best average distance of:  ' + str(best_keysize))

    print('[-] Transposing chunks...')
    transposed_chunks = transpose_bytes(raw_bytes, best_keysize)
    common_char = ord(' ')
    possible_key = bytearray()

    print('[-] Finding possible keys by single-xoring with {space} as the letter...')
    for trans_chunk in transposed_chunks:
        c = collections.Counter(trans_chunk)
        char, _ = c.most_common()[0]
        possible_key.append(char ^ common_char)

    print("[+] Possible key found: " + possible_key.decode("utf-8"))
    print("[-] Attempting to decrypted file with '" + possible_key.decode("utf-8") + "'")
    print("[+] Decrypted file: ")
    print(str(decrypt_with_key(raw_bytes, possible_key)))





