from Crypto.Cipher import AES

# key has to be 16,24 or 32 bytes long
cryptObj = AES.new('This is my key42',AES.MODE_CBC,'16 character vec')
# notice the spaces -- that's to pad it out to a multiple of 16 bytes
plaintext = "This is some text we need to encrypt because it's very secrect  "
print(len(plaintext))
ciphertext = cryptObj.encrypt(plaintext)
# print(ciphertext)

# this won't work if the key isn't identical
newcryptObj = AES.new('this is my key42',AES.MODE_CBC,'16 character vec')
result = newcryptObj.decrypt(ciphertext)
print(result)

# this will work
newcryptObj = AES.new('This is my key42',AES.MODE_CBC,'16 character vec')
result = newcryptObj.decrypt(ciphertext)
print(result)
