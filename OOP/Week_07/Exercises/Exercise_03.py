from random import randint


# Letters PW can contain
symbols = "+-*/?!@#$%&"
alphabets = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"


def main():
    password_length = int(input("Enter the length of password: "))    
    result = passwordMaker(password_length)
    print("Generated Password:", result)


## Generates a random password.
# @param length an integer that specifies the length of the password
# @return a string containing the password of the given length with one digit and one special character
#
def passwordMaker(length):
    password = ""
    
    # number of alphabets == length - (one digit + one special character) = length - 2
    for _ in range(length - 2):
        password += randomCharacter(alphabets)
    
    # one digit
    random_digit = randomCharacter(digits)
    password = insertAtRandom(password, random_digit)
    
    # one special character
    random_symbol = randomCharacter(symbols)
    password = insertAtRandom(password, random_symbol)
    
    return password


## Returns a string containing one character randomly chosen from a given string.
# @param characters the string from which to randomly choose a character
# @return a substring of length 1, taken at a random index
#
def randomCharacter(characters):
    i = randint(0, len(characters) - 1)
    return characters[i]


## Inserts one string into another at a random position.
# @param original_str the string into which another string is inserted
# @param str_to_insert the string to be inserted
# @return the string that results from inserting toInsert into string
#
def insertAtRandom(original_str, str_to_insert):
    random_index = randint(0, len(original_str))
    return original_str[:random_index] + str_to_insert + original_str[random_index:]


main()