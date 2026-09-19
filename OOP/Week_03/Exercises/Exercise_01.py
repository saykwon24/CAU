# Define some constants
PENNIS_PER_DOLLAR = 100
PENNIS_PER_QUARTER = 25


# Obtain input from user: bill in dollar and item price in penny
bill = int(input("Enter bill value (1 = $1 bill, 5 = $5 bill, etc.): "))
price = int(input("Enter item price in pennies: "))


# Compute change due
change_due = bill * PENNIS_PER_DOLLAR - price    # convert dollar to penny
num_dollars = change_due // PENNIS_PER_DOLLAR    
num_quarters = (change_due % PENNIS_PER_DOLLAR) / PENNIS_PER_QUARTER


# Print change due
print("Dollar coins: %6d" % num_dollars)
print("Quarters:     %6d" % num_quarters)
