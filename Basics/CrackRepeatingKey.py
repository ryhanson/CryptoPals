import base64
from XORLord import XORLord

def str2bin(string):
    return ''.join((bin(ord(c))[2:].zfill(8) for c in string))

def hamming_distance(str1, str2):
    distance = 0
    str1_bytes = str2bin(str1)
    str2_bytes = str2bin(str2)

    for a, b in zip(str1_bytes, str2_bytes):
        if a != b:
            distance += 1

    return distance

def raw_hamming_distance(bin1, bin2):
    distance = 0

    for a, b in zip(bin1, bin2):
        if a != b:
            distance += 1

    return distance

test_str1 = "this is a test"
test_str2 = "wokka wokka!!!"
correct_distance = 37
test_distance = hamming_distance(test_str1, test_str2)

print "[-] Validating Hamming Distance function..."
print "[-] Finding Distance Between: '" + test_str1 + "' and '" + test_str2 + "'"
print "[+] Hamming Distance Found: " + str(test_distance)
if test_distance == correct_distance:
    print "[+] Hamming Distance function is working properly!"

print "[-] Time to crack repeating XOR cipher..."


with open('6.txt', 'r') as encrypted_file:
    encrypted_contents = encrypted_file.read()
    decoded_contents = base64.b64decode(encrypted_contents)
    binary_contents = str2bin(decoded_contents)

    print "[-] Chunking bytes into sets based on KEYSIZE..."

    # Create a set of chunks for keysizes between 2 and 40
    binary_chunks = [[binary_contents[i:i+x] for i in range(0, len(binary_contents), x)] for x in range(2, 40, 1)]

    print "[+] " + str(len(binary_chunks)) + " sets of chunks created for KEYSIZEs between 2 and 40!"

    smallest_distance = 9999
    best_keysize = 0
    for chunk_set in binary_chunks:
        first_chunk = chunk_set[0]
        second_chunk = chunk_set[1]
        keysize = len(first_chunk)
        chunk_distance = raw_hamming_distance(first_chunk, second_chunk)
        normalized_distance = float(chunk_distance) / float(keysize)

        print "[-] Testing chunks with size of: " + str(keysize)
        print "[-] First chunk: " + str(first_chunk)
        print "[-] Second chunk: " + str(second_chunk)
        print "[+] Hamming distance for keysize " + str(keysize) + " is: " + str(chunk_distance)
        print "[+] Normalized distance is: " + str(normalized_distance)

        if normalized_distance < smallest_distance:
            smallest_distance = normalized_distance
            best_keysize = keysize

    print "[-] The results are in..."
    print "[+] Smallest distance keysize is " + str(best_keysize) + " with distance of: " + str(smallest_distance)

    # TODO:
    # Try taking 4 keysize blocks and averaging the distances between them
    # Bytes are already chunked, now transpose them by:
    # make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
    # Getting closer....


