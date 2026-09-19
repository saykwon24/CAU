ROWS = 6
COLUMNS = 7

# Initialize the populations table.
populations = [
    [ 106, 107, 111, 133, 221, 767, 1766 ],
    [ 502, 635, 809, 947, 1402, 3634, 5268 ],
    [ 2, 2, 2, 6, 13, 30, 46 ],
    [ 163, 203, 276, 408, 547, 729, 628 ],
    [ 2, 7, 26, 82, 172, 307, 392 ],
    [ 16, 24, 38, 74, 167, 511, 809 ]
]

# Define a list of continent names.
continents = [
    "Africa",
    "Asia",
    "Australia",
    "Europe",
    "North America",
    "South America"
]


# Print the table header.
print("                Year 1750 1800 1850 1900 1950 2000 2050")


# Create an empty list for total populations
totals = [0] * COLUMNS

# Print population data.
for row in range(ROWS):
    
    # Print the i-th row
    print("%20s" % continents[row], end="")
    for column in range(COLUMNS):
        print("%5d" % populations[row][column], end="")
        
        # Calculate the totals
        totals[column] += populations[row][column]
    
    # Start a new line at the end of the row.
    print()

# Print column totals.
print("%20s" % "World", end="")
for i in totals:
    print("%5d" % i, end="")
print()