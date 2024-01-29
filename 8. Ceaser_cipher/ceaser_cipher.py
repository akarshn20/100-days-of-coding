from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount   
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the encoded text is {cipher_text}")

# def decrypt(text, shift):
#     decipher = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         decipher += alphabet[new_position]
#     print(f"The decoded text is {decipher}")

# if direction == "encode":
#     encrypt(plain_text = text,shift_amount = shift)
# elif direction == "decode":
#     decrypt(text, shift) 

## New and easy method ##

def caesar(text, shift, direction):
  end_text = ""
  if direction == "decode":
    shift *= -1
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift
      end_text += alphabet[new_position]
    else:
      end_text += letter
  print(f"The {direction}d text is {end_text}")

print(logo)
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26 #if the user enters number greater than 26
  caesar(text, shift, direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_continue = False
    print("Goodbye")