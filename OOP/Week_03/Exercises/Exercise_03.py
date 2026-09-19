# Get a string from user
user_str = input("Enter a string: ")


# Extract the middle character(s)
index = len(user_str) // 2

if len(user_str) % 2 == 1:
    middle_str = user_str[index]
else:
    middle_str = user_str[index - 1] + user_str[index]


# Print the result
print("Middle: %s" % middle_str)