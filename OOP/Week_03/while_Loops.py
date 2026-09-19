# Week_03 (2)
"""
while Loop: executes instructions while the condition is True
    [syntax] while condition:
                 statements

Counter-Controlled Loop: execute a sequence of statements a 'definite' times by using counter variable
Event-Controlled Loop: execute until an event occurs, so doesn't know how many iterations, 'indefinite' loop
"""

# counter-controlled loop
i = 0    # counter
total = 0
while total < 10:
    i += 1
    total += 1
    print(i, total)


# event-controlled loop
TARGET = 20000.0
RATE = 0.05

balance = 10000.0
year = 0
while balance < TARGET:
    year += 1
    interest = balance * RATE / 100
    balance += interest
print("The balance is $%.2f" % balance)



"""
Common Loop Algorithms
"""

#1) Sum and Average value
total = 0.0
count = 0
input_val = float(input("Enter value: "))    # first input
while input_val != "":
    total += input_val    # sum input values until the user type ""
    count += 1
    input_val = float(input("Enter value: "))    # after the first input

if count > 0:
    average = total / input_val
else:
    average = 0.0


#2) Counting Matches: count values that fulfill a condition
negatives = 0
input_int = int(input("Enter value: "))
while input_int != "":
    if input_int < 0:
        negatives += 1    # count negative values
    input_int = int(input("Enter value: "))

print(f"There were {negatives} negative values")


#3) Prompting until a Match is found: keep asking whether the input is valid
valid = False
while not valid:
    value = int(input("Please enter a positive value < 100: "))    # keep asking by while
    if value > 0 and value < 100:
        valid = True
    else:
        print("Invalid input")


#4) Maximum and Minimum: find largest or smallest value whenever you see a larger or smaller one
largest = int(input("Enter a value: "))
input_integer = int(input("Enter a value: "))
while input_integer != "":
    if input_integer > largest:
        largest = input_integer    # update when you find larger one
    input_integer = int(input("Enter a value: "))

smallest = int(input("Enter a value: "))
input_integer = int(input("Enter a value: "))
while input_integer != "":
    if input_integer < smallest:    # just change the range
        smallest = input_integer
    input_integer = int(input("Enter a value: "))


#5) Comparing adjacent values
value = int(input("Enter a value: "))
input = int(input("Enter a value: "))
while input != "":
    previous = value
    value = input
    if value == previous:
        print("Duplicate input")
    input = int(input("Enter a value"))
