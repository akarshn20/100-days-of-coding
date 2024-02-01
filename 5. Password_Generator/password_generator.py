import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
Letters = int(input("How many letters would you like in your password? \n"))
Symbols = int(input("How many symbols would you like? \n"))
Numbers = int(input("How many numbers would you like? \n"))

password = ""

for char in range(1, Letters + 1):
    password += random.choice(letters)

for symbol in range(1,Symbols + 1):
    password += random.choice(symbols)

for number in range(1, Numbers + 1):
    password += random.choice(numbers)

print(f"Your password is: {password}")

new_password = list(password)
random.shuffle(new_password)
password1 = ""
for i in new_password:
    password1 += i
print(f"Or you can use stronger password that is: {password1}")
