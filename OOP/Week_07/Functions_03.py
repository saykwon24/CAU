# Week_07 (2)
"""
Recursive Function: one that calls 'itself'
                    recursive solution is simpler than nested loops to understand
                    
                    for recursion to be successful,
                    1) Every recursive call must simplify the task in some way
                    2) There must be special cases to handle the 'simplest tasks' directly
"""

## Prints a triangle with a given side length.
# @param side_length an integer indicating the length of the bottom row
#
def printTriangle(side_length):
    if side_length < 1: return    # special cases for simplest task
    printTriangle(side_length - 1)    # print 'smaller' row of triangle
    
    print("[]" * side_length)


# Using nested loops: same idea as above
def printTriangle(side_length):
    for i in range(side_length):
        print("[]" * i)


# reverse triangle
def printTriangle(side_length):
    if side_length < 1: return
    
    # just swap the below statements
    print("[]" * side_length)
    printTriangle(side_length - 1)