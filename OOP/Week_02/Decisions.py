# Week_02 (2)
"""
Compound Statement: span multiple lines and consist of a 'header' and a 'statement block'
                    require a colon(:) at the end of the 'header'
                    a group of statements which are the same indentation level are the 'statement block'
                    indentation is important in Python and conventionally use two or four(Tab) spaces as indent


if-else Statements: when if condition is True, execute if statements, otherwise else statements
                    if necessary, else statement can be omitted
    [syntax] if condition:
                 statements
             [else:
                 statements]

Conditional Expressions: more 'pythonic' way for if-else statements
    [syntax] value1 if condition else value2
        this means that value1 if the condition is true, value2 if the condition is false
        should not colon(:) at the end of if condition, because conditional expression is not compound expression    
"""

# Conditional Expression
floor = int(input("Enter the floor: "))
print("Actual floor:", (floor - 1) if (floor > 13) else floor)



"""
Relational Operators: compare numbers and strings
                      if both left and right are string, coming first alphabetically is 'small'
                      relational operators have 'lower' precedence than arithmetic operators
    == | equal
    != | not equal
    >  | greater than
    <  | less than
    >= | greater than or equal to
    <= | less than or equal to
"""

# Alphabetically compare from start of string to end of string
print('apple' < 'snake')    # True



"""
Comparison of Floating-point Numbers: floats are represented in computer HW as binary number
                                      unfortunately, most decimal fractions cannot be represented exactly as binary fractions
                                      so floats have only a limited precision, and float calculations can introduce 'roundoff' errors
                                      even though the printed result looks like the exact value, the actual stored value is the nearest representable binary fraction (approximation)
                                      
                                      the magnitude of two floats should be less than some threshold E (very small number)
                                      it is common to set E to 10^(-14) when comparing floating-point numbers
    >>> https://docs.python.org/3/tutorial/floatingpoint.html
"""

# Comparison of float
from math import sqrt

r = sqrt(2.0)
if r * r == 2.0:
    print("sqrt(2.0) squared is 2.0")
else:
    print(f"sqrt(2.0) squared is not 2.0 but {r * r}")



"""
Nested Branch: decision statement in decision statement (multi-level)
Multiple Alternative: multiple if-elif statements (one-level)
                      if not use 'elif' statements, branches are increased, then the code becomes difficult to read
                      must sort the conditions and test of if or elif against the 'largest' cutoff first
                      that is, test general conditions after more specific conditions (specific -> general)
                      use this when conditions are dependent each other
"""