# Week_04 (2)
"""
Container: object that contains or stores a collection of elements    (ex. string, list, dictionary, ...)

for Statement (1): can be used to iterate over the contents of any container    (ex. characters in the string)
    [syntax] for variable in container:
                 statements
        'variable' take an element of 'container'

Differences between for and while loop: while uses 'index variable' by which creates element variable
"""

state = "Virginia"
for letter in state:    # element variable
    print(letter)

# equivalent while loop as above
i = 0    # index variable
while i < len(state):
    letter = state[i]
    print(letter)
    i += 1



"""
for Statement (2): iterate over a range of integer values with 'range()' function
    range(start, stop, step=1) | generates a sequence of values less than 'stop' at intervals of 'step', starting with 'start'
                                 ending value(2nd argument 'stop') is not included in the sequence
                                 if you pass just one argument 'stop', the range of values starts at zero
"""

for i in range(1, 11, 2):
    print(i)    # 1, 3, 5, 7, 9

for i in range(10, 0, -2):
    print(i)    # 10, 8, 6, 4, 2

for i in range(10):
    print("Hello")    # print 'Hello' 10 times(0~9)



"""
Nested Loops: loop in loop, that is, the body of a loop contains another loop
              inner loop is 'nested' inside the outer loop
              typical use is printing a table with rows and columns


Positional argument: argument that can be passed based on its position in function header
Named argument: argument that can be passed based on its name in function header

print() function
    [syntax] print(*objects, sep=' ', end='\n', file=None, flush=False)
        print 'objects' to the text stream 'file', seperated by 'sep' and followed by 'end'
        'objects' is positional argument, 'sep', 'end', 'file' and 'flush' are named arguments
"""

# 3 by 4 matrix
for i in range(3):
    for j in range(4):
        print("*", end="")
    print()    # new line

# 4 by 3 matrix
for i in range(4):
    for j in range(3):
        print("*", end="")
    print()

# 4 rows of lengths 1,2,3, and 4
for i in range(4):
    for j in range(i + 1):
        print("*", end="")
    print()

# alternating * and -
for i in range(3):
    for j in range(5):
        if j % 2 == 1:    # if j is odd
            print("*", end="")
        else:
            print("-", end="")
    print()

# a checkerboard pattern
for i in range(3):
    for j in range(5):
        if i % 2 == j % 2:    # if both i and j are either odd or even
            print("*", end="")
        else:
            print(" ", end="")
    print()
