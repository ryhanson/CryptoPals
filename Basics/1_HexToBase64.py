import base64

hexed = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
solution = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

unHexed = hexed.decode("hex")
result = base64.b64encode(unHexed)

print "Does: " + result + " == " + solution

if result == solution:
    print "Yes it does!!"
