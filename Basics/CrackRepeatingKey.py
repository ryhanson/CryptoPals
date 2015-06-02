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

test_str = "this is a test"
wokka_str = "wokka wokka!!!"
edit_distance = hamming_distance(test_str, wokka_str)

print "-+= Super awesome hamming distance finder =+-"
print "[-] Finding Distance Between: '" + test_str + "' and '" + wokka_str + "'"
print "[+] Hamming Distance Found: " + str(edit_distance)
print "[-] Time to crack repeating XOR cipher..."

