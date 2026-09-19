# Obtain original price from user
original_price = float(input("Original price before discount: "))


# Determine the discount rate and calculate discounted price
if 0 < original_price < 128:
    discounted_price = original_price * 0.92    # discount 8 %
elif original_price >= 128:
    discounted_price = original_price * 0.84    # discount 16 %
else:
    print("Invalid value")


# Print discounted price
print("Discounted price: %.2f" % discounted_price)
