# Obtain the floor number from the user as an integer
try:
    floor = int(input("Enter the floor number: "))
except ValueError:
    exit("The floor number should be an integer")

# Make sure the user input is vaild
if floor == 13:
    print("Error: There is no 13th floor.")
elif not (0 < floor < 13) or (13 < floor < 20):
    print("Error: The floor number should be between 1 and 20")
else:
    if floor < 13:
        print("Floor: %d" % floor)
    else:
        print("Floor: %d" % floor - 1)
