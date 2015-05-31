def encrypt(string, key):
    encrypted = ""
    for x in range(0, len(string), 3):
        chunk = string[x:x+3]
        for y, z in zip(chunk, key):
            encrypted += chr(ord(y) ^ ord(z))

    return encrypted

lyric_lines = ["Burning 'em, if you ain't quick and nimble", "I go crazy when I hear a cymbal"]
ice_key = "ICE"

for line in lyric_lines:
    print "Encrypting: " + line
    print "Encrypted: " + encrypt(line, ice_key).encode("hex")
