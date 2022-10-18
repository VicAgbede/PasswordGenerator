"""
    Password Generator Project
    input:  password length
            Number of Digits
            Number of Symbols
    
    output: password (as string)
"""

# importing the relevant modules
import string
import random

# List of all lowercase and uppercase characters in Python
all_alphabets = list(string.ascii_letters)
#print (f"These are the alphabets of the English Language {all_alphabets}")

all_digits = list(string.digits)
#print (f"These are the digits of the English Language {all_digits}")

all_symbols = list(string.punctuation)
#print (f"These are the symbols of the English Language {all_symbols}")

# Ask user for how many letters they would like in their password and cast to integer and store as no_of_letters
no_of_letters = int(input("How many letters would you like in your password? "))
print(no_of_letters)

# Ask user for how many symbols they would like in their password and cast to integer and store as no_of_symbols
no_of_symbols = int(input("How many symbols would you like in your password? "))
print(no_of_symbols)

# Ask user for how many digits they would like in their password and cast to integer and store as no_of_digits
no_of_digits = int(input("How many digits would you like in your password? "))
print(no_of_digits)

# Set Accumulator for Password Characters List
Password_character_list = []

# Get the random letter for the password
# Randomly Select the characters
for number in range(no_of_letters):
#       select a random characer from list of alphabets and append to the password characters list 
    random_letter = random.choice (all_alphabets)
    Password_character_list.append(random_letter)
#print(Password_character_list)

# Get the Random Symbols for the password symbols

# Set Accumulator for the Number of Symbols List
Password_symbol_list = []

# Randomly Select the characters
for number in range(no_of_symbols):
#       select a random symbol from list of symbols and append to the password symbols list 
    random_symbols = random.choice (all_symbols)
    Password_symbol_list.append(random_symbols)
#print(Password_symbol_list)



# Get the Random Digits for the password

Password_digits_list = []
    
# Randomly Select the characters
for number in range(no_of_digits):
#       select a random digit from list of digits and append to the password digits list 
    random_digits = random.choice (all_digits)
    Password_digits_list.append(random_digits)
#print(Password_digits_list)

# Add the lists to get the final_password_list and shuffle the final_password_list
final_password_list = Password_character_list + Password_symbol_list + Password_digits_list
#print(final_password_list)

# To shuffle, items in a list 
random.shuffle(final_password_list)
#print(final_password_list)

# Change password in list to a string

# accumulator for string_password
string_password= " "

for character in final_password_list:
#       append the character to the string_password
    string_password += character
# Print the string password
print("Here is your password:",string_password)