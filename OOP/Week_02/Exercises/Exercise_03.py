from math import sqrt

# Define distances and speeds
dx = 10
dy = 3
l1 = 6
s1 = 5
s2 = 2

# Calculate l2
l2 = sqrt((dx - l1) ** 2 + dy ** 2)

# Calculate times for both segments
t1 = l1 / s1
t2 = l2 / s2
total_time = t1 + t2

# Print the output
print("Total travel time:", total_time)