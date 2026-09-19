# Week_05 (1)
"""
Pseudorandom numbers: numbers that are drawn from sequences of numbers that don't repeat for a long time
                      they just behave like random numbers


random Module Methods
    random.random()      | return the next random floating-point number in the range '0.0 <= X < 1.0'
    random.randint(a, b) | return a random integer N such that 'a <= N <= b'
    >>> https://docs.python.org/3/library/random.html
"""

# generate random floating point numbers between 0 and 1
from random import random

for _ in range(10):
    value = random()
    print(value)


# generate random integers
from random import randint

for _ in range(10):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(d1, d2)