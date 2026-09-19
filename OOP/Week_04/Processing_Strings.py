# Week_04 (3)
"""
Some string methods for processing strings
"""

#1) Counting Matches: count the number of matches
string = "My Fair Lady"
uppercase = 0
for char in string:
    if char.isupper():
        uppercase += 1
print("The number of uppercase letter is", uppercase)

vowels = 0
for char in string:
    if char.lower() in "aeiou":
        vowels += 1
print("The number of vowels is", vowels)


#2) Finding All Matches: print characters(matches) in a string
sentence = input("Enter a sentence: ")
for i in range(len(sentence)):
    if sentence[i].isupper():
        print(i)


#3) Finding the First or Last Match: exit the loop when the match is found
found = False
position = 0    #position = len(string) - 1
while (not found) and (position < len(string)):
    if string[position].isdigit():
        found = True
    else:
        position += 1    #position -= 1

if found:
    print("First digit occurs at position", position)
else:
    print("The string does not contain a digit")


#4) Validating a String: validate whether the string contains correctly formatted data
phone_number = input("Enter your phone number: ")
valid = len(phone_number) == 13    # precedence: = > ==
position = 0
while valid and position < len(phone_number):
    #4-1) using if statement
    if position == 0:
        valid = string[position] == "("
    elif position == 4:
        valid = string[position] == ")"
    elif position == 8:
        valid = string[position] == "-"
    else:
        valid = string[position].isdigit()
    position += 1
    
    #4-2) combining the 4 logical conditions
    valid = ((position == 0 and string[position] == "(")
              or (position == 4 and string[position] == ")")
              or (position == 8 and string[position] == "-")
              or (position != 0 and position != 4 and position != 8 and string[position].isdigit()))
    position += 1


#5) Building a New String
#5-1)remove some symbols from a string
user_input = input("Enter a credit card number: ")
card_number = ""
for char in user_input:
    if char != " " and char != "-":
        card_number += char    # concatenate characters
print("Card Number:", card_number)

#5-2) convert uppercase to lowercase, vice versa
original = "HEllo, woRLd!"
new_str = ""
for char in original:
    if char.isupper():
        new_char = char.lower()
    elif char.islower():
        new_char = char.upper()
    else:
        new_char = char
    new_str += new_char    # concatenate characters
print(new_str)    # heLLO, WOrlD!