# Week 09 (2)
"""
Tuple: data type for immutable sequences of arbitrary data
       once a tuple is created, its contents cannot be modified
       you can omit the parentheses, but prefer to use them for clarity
       any list operation that does not modify the contents of the list can be used with a tuple
    [syntax] variableName = ()
    
       use tuple to assign to multiple variables in a single assignment statement
       but the assignment can't really be simultaneous, just for readability
       also, using tuple is a convenient shortcut for swapping two values
"""

(low, high) = (5, 10)
print("Enter a value between %d and %d:" % (low, high))


# Swap two values
values = [32, 54, 67.5, 29, 35]
for i in range(len(values) - 1):
    if values[i] > values[i + 1]:
        (values[i], values[i + 1]) = (values[i + 1], values[i])
        # right hand side are first stored in a temporary tuple, and then the tuple values are assigned


# Returning multiple values with tuple
def readDate():
    print("Enter a date:")
    month = int(input(" month: "))
    day = int(input(" day: "))
    year = int(input(" year: "))
    return (month, day, year)    # return 'a' tuple, so the function has one return value (not multiple return values)

date = readDate()    # assign the entire tuple
(month, day, year) = readDate()    # assign the values in variables respectively