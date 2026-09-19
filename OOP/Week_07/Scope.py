# Week_07 (1)
"""
Scope: the part of your program in which it is visible
       a variable that is defined in a different part of your program, cannot access to the variable
       by passing the variable as an argument, can access it
       possible to use the same variable name in a different scope


Local variable: one that is defined within a code block(usually, function), can be used only within the block
Global variable: one that is defined outside of a code block, can be used wherever in your code
                 you can use a local variable as global variable by using 'global' keyword
                 
                 but, you should avoid to use global variables, because it is more difficult to understand when many functions modify it
                 instead of using global variables, use function parameter variables and return value
                 Global constants, however, are fine to use and put them at the top of your code
"""

balance = 10000    # global variable

def withdraw(amount):
    global balance    # This function intends to update the value of 'balance'
    if balance >= amount:
        balance -= amount
