def main():
    scores = readFloats()
    
    if len(scores) > 1 :
        removeMinimum(scores)
        removeMinimum(scores)
        total = sum(scores)
        print("Final score:", total)
    
    else :
        print("At least two scores are required.")


## Reads a sequence of floating-point numbers.
# @return a list containing the numbers
#
def readFloats():
    # Create an empty list
    values = []
    
    # Read the input values into a list
    value = input("Enter a series of quiz scores (seperated by spaces):\n")
    
    # Check for quit command and handle empty input
    if (value.upper() == "Q") or (value.strip() == ""): return []
    
    for i in value.split(" "):
        values.append(float(i))
    
    return values


## Removes the minimum value from a list.
# @param values a list of size >= 1
#
def removeMinimum(values):
    minimum = min(values)
    values.remove(minimum)
    # No return is needed since lists are modified in-place


main()