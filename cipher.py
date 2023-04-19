from string import ascii_uppercase, ascii_letters


class Cipher:

  def __init__(self):
    self.alphabet = list(ascii_uppercase)

    # for letter in ascii_uppercase:
    #   list.append(letter)

    # [letter for letter in ascii_uppercase]
    # list = ['A','B','C'...]
    # self.alphabet =

  def encrypt_message(self, message):
    message = message.upper()
    # upper(), lower() capitalize() - first letter become upper case\
    message = list(message)
    # how to set up a for loop to read our message list by index, cannot use for letter in message, we have to use something else
    # access letter, message[0]
    # new Location = 25 - original_location
    # new letter would be, self.alphabet[25 - original location]
    for i in range(len(message)):
      #use all elements from array, to create a string, where we put the connecting letter in between '', where ''.join(list) is the statement
      if message[i] in self.alphabet:
        message[i] = self._encrypt_letter(message[i])

    return "".join(message)

  def decrypt_message(self, message):
    message = message.upper()
    # upper(), lower() capitalize() - first letter become upper case\
    message = list(message)
    # how to set up a for loop to read our message list by index, cannot use for letter in message, we have to use something else
    # access letter, message[0]
    # new Location = 25 - original_location
    # new letter would be, self.alphabet[25 - original location]
    for i in range(len(message)):
      #use all elements from array, to create a string, where we put the connecting letter in between '', where ''.join(list) is the statement
      if message[i] in self.alphabet:
        message[i] = self._decrypt_letter(message[i])

    return "".join(message)

  def _encrypt_letter(self, letter):
    original_location = self.alphabet.index(letter)
    new_location = 25 - original_location
    new_letter = self.alphabet[new_location]
    return new_letter

  def _decrypt_letter(self, letter):
    new_location = self.alphabet.index(letter)
    original_location = 25 - new_location
    original_letter = self.alphabet[original_location]
    return original_letter
