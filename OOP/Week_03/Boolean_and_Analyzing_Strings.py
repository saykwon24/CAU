# Week_03 (1)
"""
Boolean type: means True or False, these are special type of value (not str or int)
              should write the title in uppercase
Boolean operator (precedence: relational operator > boolean operator / and > or)
    and | return True when left and right side are all True (two operands)
    or  | return True when either left or right side are True (two operands)
    not | return True when the operand in right side is False (one operand)
"""

x = float(input("Enter random number: "))
if x > 10 and x < 15:
    print("x is larger than 10 and less than 15")
else:
    print(f"x is {x}")



"""
Analyzing strings: determine whether a string contains a given substring
    Membership Operators
        in     | return True when the right side is in the left side
        not in | return True when the right side is not in the left side
    
    String Methods
        str.count(substring)      | return the number of 'substring' in 'str'
        str.find(substring)       | return the lowest index of 'substring' in 'str' or -1 when 'substring' does not exist
        str.startswith(substring) | return True when 'str' begins with 'substring'
        str.endswith(substring)   | return True when 'str' ends with 'substring'
        
        str.isalnum() | return True when 'str' only contains one more letters and digits
        str.isalpha() | return True when 'str' only contains one more letters
        str.isdigit() | return True when 'str' only contains one more digits
        str.isspace() | return True when 'str' only contains one more whitespaces(space, new line, tab, ...)
        str.islower() | return True when all letters in 'str' is lowercase
        str.isupper() | return True when all letters in 'str' is uppercase
        >>> https://docs.python.org/3/library/stdtypes.html#str
"""

# using membership operator
name = "John Wayne"
if "Way" in name:
    print("true.")

if "-" not in name:
    print("- is not in the name")


# using string method
filename = "file1.txt"
if filename.endswith(".txt"):
    print("It is text file")

name = "John Johnson"
print(name.find("oh"))    # print the index of first substring 'o'


# lexicographical ordering of strings: uppercase precedes lowercase
print('john' < 'John')    # False
