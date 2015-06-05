import base64
import collections
from XORLord import XORLord

def hamming_dist(a, b):
    xored = bytes([x ^ y for (x, y) in zip(a, b)])

    return sum((xored[j] >> i) & 1 for i in range(8) for j in range(len(xored)))

def get_avg_hamming_dist(raw, chunk_size):
    chunks = get_chunks(raw, chunk_size)

    return sum(hamming_dist(c1, c2) / chunk_size for c1, c2 in zip(chunks, chunks[1:])) / len(chunks[1:])

def get_chunks(raw, chunk_size):
    return [raw[i:i+chunk_size] for i in range(0, len(raw), chunk_size)]

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
    for keysize in range(2, 40):
        avg_distance = get_avg_hamming_dist(raw_bytes, keysize)

        if avg_distance < best_average:
            best_average = avg_distance
            best_keysize = keysize

    print('smallest distance ' + str(best_average) + ' was found with chunk size ' + str(best_keysize))

    transposed_chunks = [raw_bytes[r::best_keysize] for r in range(best_keysize)]
    common_char = ord(' ')
    possible = bytearray()

    for trans_chunk in transposed_chunks:
        c = collections.Counter(trans_chunk)
        char, _ = c.most_common()[0]
        possible.append(char ^ common_char)

    key = possible.decode("utf-8")

    print(key)

    xoring = XORLord()
    xoring.encrypted = decoded

    print(xoring.encrypted[0])

    decrypted = xoring.decrypt_with_key(key)

    print(decrypted)





