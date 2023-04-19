# inheritance
from cipher import Cipher
class CaesarCipher(Cipher):
  def __init__(self, shift):
    ##super() -> call class Cipher
    super().__init__()
    self.shift = shift
  # polymorphism 
  def _encrypt_letter(self, letter):
    original_location = self.alphabet.index(letter)
    # to prevent overflow 
    
    new_location = (original_location + self.shift) % 26
    new_letter = self.alphabet[new_location]
    return new_letter
  # polymorphism 
  def _decrypt_letter(self, letter):
    new_location = self.alphabet.index(letter)
    original_location = (new_location - self.shift) % 26
    original_letter = self.alphabet[original_location]
    return original_letter