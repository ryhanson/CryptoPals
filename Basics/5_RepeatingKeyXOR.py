from XORLord import XORLord

ice_key = "ICE"

print "Encrypting/Decrypting each line: "

lyric_lines = ["Burning 'em, if you ain't quick and nimble", "I go crazy when I hear a cymbal"]

for line in lyric_lines:
    encrypt_lord = XORLord(line)
    print "Original: " + encrypt_lord.plain
    print "Encrypted: " + encrypt_lord.encrypt_with_key(ice_key, return_hex=True)
    print "Decrypted: " + encrypt_lord.decrypt_with_key(ice_key)

print "Encrypting/Decrypting combined lyrics: "

full_lyrics = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
full_xor = XORLord(full_lyrics)

print "Original:\n" + full_lyrics
print "Encrypted:\n" + full_xor.encrypt_with_key(ice_key, return_hex=True)
print "Decrypted:\n" + full_xor.decrypt_with_key(ice_key)
