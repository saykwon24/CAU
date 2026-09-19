from random import random

TRIES = 10000
hits = 0

for i in range(TRIES):
    # Generate two random numbers between -1 and 1
    x = random() * 2 - 1
    y = random() * 2 - 1
    
    # Check whether the point lies in the unit circle
    if (x**2 + y **2) <= 1: hits += 1

# The ratio hits/tries is approximately the same as the ratio
piEstimate = 4 * hits / TRIES
print("Estimate for pi:", piEstimate)