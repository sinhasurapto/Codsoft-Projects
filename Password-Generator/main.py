import random

# List of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Ask for number of letters, numbers, symbols
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Password string
pwd = ''

# Password list
pwdList = []

# Letters are append to password list
for num in range(0, nr_letters):
    pwdList.append(random.choice(letters))

# Symbols are append to password list
for num in range(0, nr_symbols):
    pwdList.append(random.choice(symbols))

# Numbers are append to password list
for num in range(0, nr_numbers):
    pwdList.append(random.choice(numbers))

# Shuffle the password list
random.shuffle(pwdList)

# Append characters of password list to password string
for ch in pwdList:
    pwd += ch

# Display password
print(f"Your password is:{pwd}")
