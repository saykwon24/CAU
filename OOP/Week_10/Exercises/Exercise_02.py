def main():
    numbers = readFloats(5)
    multiply(numbers, 10)
    printReversed(numbers)



## Reads a sequence of floating-point numbers.
# @param numberOfInputs the number of inputs to read
# @return a list containing the input values
#
def readFloats(numberOfInputs):
    user_inputs = []
    
    print("Enter 5 numbers:")
    for _ in range(numberOfInputs): user_inputs.append(float(input("")))
    
    return user_inputs



## Multiplies all elements of a list by a factor.
# @param values a list of numbers
# @param factor the value with which element is multiplied
#
def multiply(values, factor):
    for i in range(len(values)): values[i] *= factor



## Prints a list in reverse order.
# @param values a list of numbers
#
def printReversed(values) :
    # Traverse the list in reverse order, starting with the last element
    print(values[::-1])
    "sequence[start:stop:step]"
    
    """
    ## another method
    i = len(values) = 1
    while i >= 0:
        print(values[i], end="")
        i -= 1
    print()
    """



# Execute the program
main()