# Initialize constants for the tax rates and rate limits
TAX_RATE1 = 0.1
TAX_RATE2 = 0.25
LIMIT1 = 32000
LIMIT2 = 64000

# Read income and marital status
income = float(input("Please enter your income: "))
is_marital = input("Please enter s for single, m for married: ")

# Compute taxes due
if is_marital == "s":
    if 0 < income <= LIMIT1:
        tax = income * TAX_RATE1    
    else:
        tax = (LIMIT1 * TAX_RATE1) + ((income - LIMIT1) * TAX_RATE2)
elif is_marital == "m":
    if 0 < income <= LIMIT2:
        tax = income * TAX_RATE1
    else:
        tax = (LIMIT2 * TAX_RATE1) + ((income - LIMIT2) * TAX_RATE2)
else:
    print("Invalid input")

# Print the result
print("Total tax: $%.2f" % tax)