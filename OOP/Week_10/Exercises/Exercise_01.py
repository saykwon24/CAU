# Create an empty list
values = []

# Read the input values
print("Please enter values, Q to quit:")
userInput = input("")
while userInput.upper() != "Q":
    values.append(float(userInput))
    userInput = input("")

# Find the largest value
largest = values[0]
for i in range(1, len(values)):
    if values[i] > largest: largest = values[i]

# Print all values, marking the largest
for value in values:
    if value == largest: print(value, "<== largest value")
    else: print(value)