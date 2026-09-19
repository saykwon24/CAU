# Week 09 (1)
"""Common List Algorithms"""

#1) Filling: the loop creates and fills a list
values = []
for i in range(5):
    values.append(i * i)



#2) Combining List Elements: concatenate strings in the list to one long string
friends = ["Harry", "Amy", "Ron", "Emily", "Bob"]
result = ""
for element in friends:
    result += element



#3) Element Separators: one fewer separator than the number of elements
result = ""
for i in range(len(friends)):
    if i > 0: result += ", "
    result += friends[i]

values = [32, 54, 67.5, 29, 35]
for i in range(len(values)):
    if i > 0: print(" | ", end="")
    print(values[i], end="")
str(values)    # returns a string in the form like list, but the type is 'str'



#4) Maximum and Minimum: you can implement this algorithm with max() or min() functions
largest = values[0]
for i in range(1, len(values)):    # except the first element
    if values[i] > largest: largest = values[i]

smallest = values[0]
for i in range(1, len(values)):
    if values[i] < smallest: smallest = values[i]


# Find alphabetically(highest in the dictionary order) first string
names = ["Ann", "Charlotte", "Zachary", "Bill"]
max(names)    # 'Ann'


# Find the longest string in the list
longest = names[0]
for i in range(1, len(names)):
    if len(names[i]) > len(longest): longest = names[i]



#5) Linear(Sequential) Search: search for the position of a specific element, or inspect the elements in sequence until a match is found
searchedValue = 100
if searchedValue in values:
    pos = values.index(searchedValue)
    print("Found at position")
else:
    print("Not found")


# Find the position of a value that has a given property
limit = 100
pos = 0
found = False
while (pos < len(values)) and (not found):
    if values[pos] > limit: found = True
    else: pos += 1
if found: print("Found at position:", pos)
else: print("Not found")



#6) Collecting and Counting Matches
# to know all matches, append them to an initially empty list
limit = 100
result = []
for element in values:
    if element > limit: result.append(element)


# to know how many matches without collecting them, use counter variable
limit = 100
counter = 0
for element in values:
    if element > limit: counter += 1



#7) Removing Matches
words = ["Welcome", "to", "the", "island"]
i = 0
while i < len(words):    # don't always increment the index, use while loop instead of for loop
    word = words[i]
    # after removing element, skipping past the next element, so use if-else statement
    if len(word) < 4: words.pop(i)
    else: i += 1



#8) Swapping Elements: use temporary variable
for i in range(len(values) - 1):
    if values[i] > values[i + 1]:
        temp = values[i]
        values[i] = values[i + 1]
        values[i + 1] = temp



#9) Reading Input: store user input in a list for later processing
values = []
print("Please enter values, Q to quit:")
userInput = input("")
while userInput.upper() != 'Q':
    values.append(float(userInput))
    userInput = input("")


""""
Using Lists with Functions: list can occur as function arguments and return values
                            when calling a function with a list argument, the function receives a list reference, not a copy of the list
                            i.e. Python assigns the memory space automatically, so the list is exist as long as there is a variable that points out the address of the list
"""

def sum(values):
    total = 0
    for element in values: total += element
    return total

def multiply(values, factor):
    for i in range(len(values)):
        values[i] *= factor    # possible to modify the elements of a list

def squares(n):
    result = []
    for i in range(n): result.append(i * i)
    return result
