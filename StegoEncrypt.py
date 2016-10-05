from Crypto.Cipher import AES
from  PIL import Image
import stepic
import binascii

# key has to be 16,24 or 32 bytes long
cryptObj = AES.new('This is my key42',AES.MODE_CBC,'16 character vec')
# notice the spaces -- that's to pad it out to a multiple of 16 bytes
plaintext = "This is some text we need to encrypt because it's very secrect  "
ciphertext = cryptObj.encrypt(plaintext)

# we need to convert to ASCII to store it nicely

binval = binascii.b2a_basey4(ciphertext)
i = Image.open('bullpuppies.jpg')

print('ASCII: ',binval)
steg = stepic.encode(i,binval)
stego.save('stegecrypt.bmp','BMP')

newim = Image.open('stegecrypt.bmp')
data = stepic.decode(newim).rstrip('\n')

print('What we have out: ',data)
# convert from  ASCII  back to binary
encrypted = binascii.a2b_base64(data)

newcryptObj = AES.new('This is my key42',AES.MODE_CBC,'16 character vec')
result = newcryptObj.decrypt(ciphertext)
print(result)

