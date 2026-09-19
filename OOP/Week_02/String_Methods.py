# Week_02 (1)
"""
Object: a software 'entity' that represents a value with certain behavior
Method: a function(collection) of programming instructions that carry out a particulat task
        can only be applied to an object of the type for which it was defined (a function of a class)
        method calls can have arguments and don't change the contents of the variable
        can use methods by using 'dot noation'
            [syntax] object.methodName(arguments)

String Methods
    str.upper()             | make 'str' uppercase
    str.lower()             | make 'str' lowercase
    str.replace(str1, str2) | replace 'str1' with 'str2', and then return a new string
                              'str1' and 'str2' are in 'str'
    >>> https://docs.python.org/3/library/stdtypes.html#str
"""

name1 = "Harry"
name2 = name1.replace("H", "G")
print(name2)



"""
User Input: read the keyboard input by using input() function
    input(prompt) | a function that display 'prompt' to user, read a value user entered in command line, and then return the value
                    user's input is considered as type "str"


Formatted Output: how to display the result of computation in any way we want
                  specifies how the string is to be formatted
    [syntax] formatstring % (value1, value2, ...)
        'format string' is the combination of 'literals' and 'format specifier'
        'format specifier' consists of string format operator '%' and so on    >>> "%-A.Bf"
            '%' is string format operator when the left side is string
            '-' means left alignment in field width, otherwise right alignment [default]
            a number A after % or - is 'field width'
            a number B after dot(.) or decimal point is 'significant digits'
            a character at the end of format specifier is the type of value: 'f' means floating-point value, 'd' means integer, 's' means string

        format string can contain one or more literals and format specifiers
        if the number of format specifiers is more than 2, you must enclose values in parentheses and seperate by commas
        and the values are used in the order listed
        format specifier is replaced with 'value'
        if you want to display % sign, just write '%%'
"""

bottles = int(input("The number of bottles: "))    # should convert str to int by using int() function
price = float(input("Price per bottle: "))         # should convert str to float by using float() function

print("The price is %10.2f" % price)    # %10.2f: format specifier
                                        # 10 field width, 2 significant digits, f(float) form
print("Total price of %5d bottles is %10.2f" % (bottles, bottles * price))
