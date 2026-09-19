# Initialize constants for shipping cost
CONTINENTAL = 5
OTHER = 10

# Obtain the user input
country = input("Enter the country: ")
state = input("Enter the state or province: ")

# Compute the shipping cost
if country == "USA":
    if state == "Hawaii" or state == "Alaska":
        tup = (state, country, OTHER)
    else:
        tup = (state, country, CONTINENTAL)
else:
    tup = (state, country, OTHER)

# Print the result
print("Shipping cost to %s, %s: $%.2f" % tup)