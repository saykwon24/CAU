# Week_01 (3)
"""
Character: a single word
String: sequence of characters
        specified by enclosing within a pair of single or double quotes (ex. 'hello', "hello")
        both types of quotes must be the pair, respectively
        ** you can include quotation mark in string by allowing both types of quotes
        empty string: "" or ''
        
        the length of string is the number of characters in it
        empty string's length is 0
        you can check the length of string by "len() function"
"""

# How to print quotation mark in string
print("He said 'Hello'")



"""
Operator Overloading: some operator can perform multiple roles by data type of values
    str1 + str2 | concatenate 'str1' and 'str2' with no space (no seperate)
                  if either str1 or str2 is int or float, python raises "TypeError"
    str * int   | repeat 'str' 'int'-times, you can locate both vice versa, but conventionally 'str' locates in the left-side
    str % int   | string format operator
    ...
"""

# + operator overloading
first = "Harry"
last = "Morgan"
name = first + "" + last    # concatenate strings with space


# * operator overloading
message = "Echo..."
print(message * 5)    # repeat 5 times



"""
Casting: function that converts data's type temporarily
         spaces at the front or back in string will be ignored
         if an invalid argument is passed, Python raises "ValueError"
    int(x)   | convert 'x' to int type
    float(x) | convert 'x' to float type
    str(x)   | convert 'x' to str type
"""

value1 = int(" 1729   ")
value2 = float("     17.29  ")
print(value1, value2, sep="\n")    # spaces in string are ignored



"""
Index: position for elements of iterable
       all indices start with index 0 (first element has index 0)
       you can access iterable's index by using square braket([])
       the index value must be within the valid range, otherwise "IndexError"
"""

first = "Rodolfo "    # whitespace's index is 7
second = "Sally"
print(first[0] + 
      "&" + second[0])    # R&S
                          # no need to be in one line as long as it's in parentheses


# Index using len() function
name = "Harry"
last = name[len(name) - 1]    # should subtract 1, because index start with 0
print(last)
