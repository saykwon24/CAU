# Week 09 (3)
"""
*args: a parameter that can receive any number of arguments
       the asterisk(*) indicates that the function can receive arbitrary number of positional arguments
       all positional arguments passed to the function are collected into a tuple named 'args'
       function can also be defined to receive a fixed number of arguments followed by arbitrary number of arguemnts
       in this case, *args must be in the last position
"""

def sum(*values):    # arguments are stored in tuple 'values'
    total = 0
    for element in values: total += element
    return total