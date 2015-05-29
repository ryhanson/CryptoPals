buffer1 = "1c0111001f010100061a024b53535009181c"
buffer2 = "686974207468652062756c6c277320657965"
solution = "746865206b696420646f6e277420706c6179"

def fixed_xor(str1, str2):
    bin_1 = str1.decode("hex")
    bin_2 = str2.decode("hex")
    xored = ""

    for x, y in zip(bin_1, bin_2):
        xored += (chr(ord(x) ^ ord(y)))

    # Super awesome shorthand version: return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(bin_1, bin_2))

    return xored

result = fixed_xor(buffer1, buffer2).encode("hex")

print "Does: " + result + " == " + solution

if str(result) == str(solution):
    print "Yes it does!!"
