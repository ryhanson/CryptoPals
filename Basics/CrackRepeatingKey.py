import base64
from XORLord import XORLord

def str2bin(string):
    return ''.join((bin(ord(c))[2:].zfill(8) for c in string))

def bin2str(bin_text):
    return ''.join(chr(int(bin_text[b:b+8], 2)) for b in xrange(0, len(bin_text), 8))

def hamming_distance(str1, str2):
    distance = 0
    str1_bytes = str2bin(str1)
    str2_bytes = str2bin(str2)

    for a, b in zip(str1_bytes, str2_bytes):
        if a != b:
            distance += 1

    return distance

def average_distance(chunks, count):
    total = 0

    for a in range(0, count, 2):
        total += hamming_distance(chunks[a], chunks[a+1])

    return float(total) / count

def raw_hamming_distance(bin1, bin2):
    distance = 0

    for a, b in zip(bin1, bin2):
        if a != b:
            distance += 1

    return distance

def raw_average_distance(chunks, count):
    total = 0

    for a in range(0, count, 2):
        total += raw_hamming_distance(chunks[a], chunks[a+1])

    return float(total) / count

def transpose_chunks(chunks, chunk_size):
    trans_chunks = []

    for s in range(0, chunk_size, 1):
        trans_chunk = ""

        for ch in chunks:
            if len(ch) == chunk_size:
                trans_chunk += ch[s]

        trans_chunks.append(trans_chunk)

    return trans_chunks

def singlebyte_decrypt(hex_str, key):
    return "".join(chr(int(hex_str[h:h+2], 16) ^ key) for h in range(0, len(hex_str), 2))


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
    xor_lord = XORLord()
    encrypted_contents = encrypted_file.read()
    decoded_contents = base64.b64decode(encrypted_contents)
    # binary_contents = str2bin(decoded_contents)

    print "[-] Chunking cipher into sets based on KEYSIZE..."

    # Create a set of chunks for keysizes between 2 and 40
    # binary_chunks = [[binary_contents[i:i+x] for i in range(0, len(binary_contents), x)] for x in range(2, 40, 1)]
    cipher_chunks = [[decoded_contents[i:i+x] for i in range(0, len(decoded_contents), x)] for x in range(2, 40, 1)]

    # print "[+] " + str(len(binary_chunks)) + " sets of chunks created for KEYSIZEs between 2 and 40!"
    print "[+] " + str(len(cipher_chunks)) + " sets of chunks created for KEYSIZEs between 2 and 40!"

    smallest_distance = 9999
    best_keysize = 0
    # for chunk_set in binary_chunks:
    for chunk_set in cipher_chunks:
        first_chunk = chunk_set[0]
        second_chunk = chunk_set[1]
        keysize = len(first_chunk)
        # chunk_distance = raw_hamming_distance(first_chunk, second_chunk)
        chunk_distance = hamming_distance(first_chunk, second_chunk)
        normalized_distance = (float(chunk_distance) / keysize)

        print "[-] Testing chunks with size of: " + str(keysize)
        print "[-] Chunk[0]: " + str(str2bin(first_chunk))
        print "[-] Chunk[1]: " + str(str2bin(second_chunk))
        print "[+] Hamming distance for keysize " + str(keysize) + " is: " + str(chunk_distance)
        print "[+] Normalized distance is: " + str(normalized_distance)

        if normalized_distance < smallest_distance:
            smallest_distance = normalized_distance
            best_keysize = keysize

    print "[-] The results are in..."
    print "[+] Smallest distance keysize is " + str(best_keysize) + " with distance of: " + str(smallest_distance)
    print "[-] Lets try average between 4 chunks..."

    smallest_avg_distance = 9999
    best_avg_keysize = 0
    # for chunk_set in binary_chunks:
    for chunk_set in cipher_chunks:
        chunk_count = 4
        # average = raw_average_distance(chunk_set, chunk_count)
        average = average_distance(chunk_set, chunk_count)
        avg_keysize = len(chunk_set[0])
        normalized_average = (float(average) / avg_keysize)

        print "[-] Testing chunks with size of: " + str(avg_keysize)

        for x in range(0, chunk_count, 1):
            print "[+] Chunk["+str(x)+"]: " + str(str2bin(chunk_set[x]))

        print "[+] Average distance between " + str(chunk_count) + " chunks is: " + str(average)
        print "[+] Normalized average distance is: " + str(normalized_average)

        if normalized_average < smallest_avg_distance:
            smallest_avg_distance = normalized_average
            best_avg_keysize = avg_keysize

    print "[-] Results for averaging 4 chunks..."
    print "[+] Smallest avg distance keysize " + str(best_avg_keysize) + " with distance of: " + str(smallest_avg_distance)
    print "[+] Best possible keysizes are: " + str(best_keysize) + " and " + str(best_avg_keysize)

    print "[-] Transposing " + str(best_keysize) + " keysize chunk set..."
    # best_chunk_set = binary_chunks[best_keysize - 2]
    best_chunk_set = cipher_chunks[best_keysize - 2]
    best_trans_set = transpose_chunks(best_chunk_set, best_keysize)
    print "[+] Chunks transposed!"

    print "[-] Transposing " + str(best_avg_keysize) + " keysize chunk set..."
    # best_avg_chunk_set = binary_chunks[best_avg_keysize - 2]
    best_avg_chunk_set = cipher_chunks[best_avg_keysize - 2]
    best_avg_trans_set = transpose_chunks(best_avg_chunk_set, best_avg_keysize)
    print "[+] Chunks transposed!"

    chunk_words = []
    for chunk in best_avg_chunk_set:
        # chunk_str = bin2str(chunk)

        for k in range(0, 255, 1):
            hex_decrypted = singlebyte_decrypt(chunk.encode("hex"), k)
            words_found = xor_lord.find_words(hex_decrypted)
            if len(words_found):
                chunk_words.append(words_found)

    print chunk_words

    # NOTE: May have to work with ciphered chunks rather than binary chunks...
    #       So after calculating distance go back to use base64 decoded ciphered text
    #       Or maybe we work convert each chunk back to chr() and decrypt that way?
    #       Hmmmmmmm........

