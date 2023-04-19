from string import ascii_uppercase, ascii_letters, ascii_lowercase
from cipher import Cipher
from caesarcipher import CaesarCipher
print([1,2,3,4])

print("+".join(['1','2','3','4']))

c = Cipher()
cc = CaesarCipher(99)
print(c.encrypt_message("Jungkook"))
print(c.decrypt_message(c.encrypt_message("Jungkook")))
print(cc.encrypt_message("Jungkook"))
print(cc.decrypt_message(cc.encrypt_message("Jungkook")))