# Week_05 (3)
"""
Return Values
    use return statement for handling exceptional cases
    every case should return a value, but if not, compiler will 'not' report it as an error
    instead, the special value 'None' will be returned
    can avoid multiple return statements by using a variable for returning value
"""

# Handling exceptional cases
def cubeVolume(sideLength):
    # exceptional case
    if sideLength < 0:
        return 0
    # regular case
    return sideLength ** 3


# return None when none-if cases
def cubeVolume(sideLength):
    if sideLength >= 0:
        return sideLength ** 3


# use 'volume' as variable for returning value
def cubeVolume(sideLength):
    if sideLength >= 0:
        volume = sideLength ** 3
    else:
        volume = 0
    return volume


# Function without Return Value: no return value (actually, return None), just print the output
def boxString(contents):
    n = len(contents)
    if n == 0: return    # return immediately
    print("-" * (n + 2))
    print("!" + contents + "!")
    print("-" * (n + 2))



"""
Using Single-Line Compound Statements
    when the function's body only contain a single statement, compound statements can be written in a single line
    this is easy to read
"""

def cubeVolume(sideLength): return (sideLength ** 3) if sideLength >= 0 else 0
print(cubeVolume(10))



"""
Reusable Functions: eliminate replicated code or pseudocode by defining a function
"""

def main():
    print("Please enter a time: hours, then minutes.")
    hours = readIntUpTo(0, 23)
    minutes = readIntUpTo(0, 59)
    print("You entered %d hours and %d minutes" % (hours, minutes))


## Prompts a user to enter a value within a given range until the user provides a valid input.
#  @param low an integer indicating the smallest allowable input
#  @param high an integer indicating the largest allowable input
#  @return the integer value provided by the user (between low and high, inclusive)
#
def readIntUpTo(low, high):
    value = int(input("Enter a value between 'str(low) + ' and ' + str(high) + ': "))
    while value < low or value > high:
        print("Error: value out of range")
        value = int(input("Enter a value between 'str(low) + ' and ' + str(high) + ': "))
    return value


main()