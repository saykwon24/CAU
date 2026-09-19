# Create constants
INIT_BALANCE = 10000
INTEREST = 0.05
TARGET = INIT_BALANCE * 2

# Initialize variables used with the loop
balance = INIT_BALANCE
year = 0

# Count the uears required for the investment to double
while balance < TARGET:
    balance = balance * (1 + INTEREST)
    year += 1

# Print the result
print("The investment doubled after %d years" % year)