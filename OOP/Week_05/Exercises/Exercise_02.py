# Print table header
print("%10d%10d%10d%10d" % (1, 2, 3, 4))
print("%10s%10s%10s%10s" % ('x ', 'x ', 'x ', 'x '))
print(' ' * 6 + '-' * 35)

# Print table body
for x in range(1, 11):
    x1 = x
    x2 = x ** 2
    x3 = x ** 3
    x4 = x ** 4
    print("%10d%10d%10d%10d" % (x1, x2, x3, x4))


# =============================================================
# using nested for loops
NMAX = 4     # columns
XMAX = 10    # rows

for n in range(1, NMAX + 1):
    print("%10d" % n, end="")

print()
for n in range(1, NMAX + 1):
    print("%10s" % 'x ', end="")

print("\n", " " * 6, "-" * 35)


for x in range(1, XMAX + 1):
    for n in range(1, NMAX + 1):
        print("%10f" % x ** n, end="")
    print()