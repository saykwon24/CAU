# Week_01 (1)
"""
Initializing a Variable
    [syntax] variableName = value
        assignment operator '=': just assign right-side to left-side, not means equality
        variable is created and initialized with that value, and can be replaced with a new value
    

Variable Name Rules
    1) must start with letter or underscore(_)
    2) can only contain letters, numbers, and underscore
    3) case sensitive
    4) can't use keywords(reserved words) as variable name
    conventionally...
    5) use a descriptive name; word boundaries are uppercase (ex. cansPerPack)
    6) start with lowercase letter, uppercase means user-defined data types
    7) all uppercase means CONSTANT


Constant: Python doesn't provide an explicit mechanism for making a variable as constant
          that is, doesn't raise an error for constant, it's up to programmers
          so all capital letters mean constant (ex. BOTTLE_VOLUME = 20)


Comment: explainations for your code
         the interpreter ignores everything from a # delimiter to the end of the line
         commonly use the comment at the top of your code
    [syntax] #        | one-line comment
             ''' '''  | multi-line comment (strictly, this is called "docstring")


Number Data Types: associated with value, not variable
                   number literal (number 그대로 받아들인다는 의미)
                   Exponential Notation always have type 'float' (ex. 2.96E-2, -3.15e10, ...)
                   "type()" function allows you to know data's type
    int   | integer, without fractional part
    float | floating-point numbers, with fractional part
        >>> int:   https://docs.python.org/3/library/functions.html?highlight=float#int
        >>> float: https://docs.python.org/3/library/functions.html?highlight=float#float
"""

print(type(6))         # int
print(type(3.14))      # float
print(type("3.14"))    # str