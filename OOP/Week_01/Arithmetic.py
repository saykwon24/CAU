# Week_01 (2)
"""
Operators: symbols for arithmetic operations
           operators with same precedence are executed 'left-to-right'
           but exponential operator ** is 'right-to-left'
Expression: combination of variables, literals, operators, and parentheses
            mixing int and float values yields a value with type 'float' (ex. 7 + 4.0 == 11.0)

Operators
    +  | addition
    -  | subtraction
    *  | multiplication
    /  | division
    ** | power (exponential operator)
    // | round down to nearest integer (floor division)
    %  | compute the remainder of floor division (modulus)
    ...
    >>> precedence: () -> ** -> *, / -> +, -
"""

print(7 // 4)    # 1
print(7 % 4)     # 3

print(-1729 // 10)    # floor -172.9 to -173

print(5 * 2 ** 3)    # same as 5 * (2 ** 3), because ** has high precedence



"""
Function: collection of programming instructions that carry out a particular task
          functions take some "argument" or not
    >>> Python built-in functions: https://docs.python.org/3/library/functions.html

Built-in Arithmetic Functions
    abs(x)                   | return absolute value of 'x'
    round(number[, ndigits]) | round 'number' to 'ndigits' below the decimal point
    max(iterable, ...)       | return the largest item in 'iterable' or the largest of 2 or more arguments
    min(iterable, ...)       | return the smallest item in 'iterable' or the smallest of 2 or more arguments
    len(obejct)              | return the length of 'object'
    ...

Another Built-in Functions
    dir(x) | display methods in terminal that can apply to 'x'
    ...
"""

distance = abs(-173)    # "pass" -173 to abs() function, and "call" the function
print("The distance from the origin is", distance)



"""
Library: code 'file' that can be used in other programs
         collection of code that written by someone else or you
Standard Library: library that is part of the language and must be included with any Python system
                  Python's standard library is organized into "modules"
Module: library that contains related functions, data types and so on
        functions in module/library must be explicitly loaded into your program by using "import" keyword
        it conventionally locates at the top of your program
            [syntax] import Module               | loading the whole 'Module' to my program, and then need to use "dot notation" for using it
                     from Module import Function | loading 'Function' in 'Module' to my program

Mathematical Functions in math module
    math.sqrt(x) | square root of 'x'
    math.pi      | means the constant '3.141592...' in math module
    ...
    >>> https://docs.python.org/3/library/math.html
"""

# math module
from math import sqrt
print(sqrt(100))

import math
print(math.sqrt(100))    # need to use "dot notation"


# square root using exponential operator **
print(4 ** (1/2))
