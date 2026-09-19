# Week 11 (4)

""" A Dictionary of Sets """
book_index = {
    "example": {7, 10}, 
    "index": {7}, 
    "program": {7, 11},
    "type": {6, 8},
    "set": {20}
}



"""
A Dictionary of Lists
    consider the problem of extracting data from a text file that represents the yearly sales 
    of different ice cream flavors in multiple stores of a retail ice cream company
"""
# Open a text file
file = open("ice_cream.txt", "r")

# Create a dictionary of lists
yearly_sales = {}
for line in file:
    parts = line.split(":", 1)    # parts == "vanila", "8580.0:7201.25:8900.0"
    flavor = parts[0]
    sales = []
    for sale in list(parts[1].strip().split(":")):
        sales.append(float(sale))    # sales == [8580.0, 7201.25, 8900.0]
    
    yearly_sales[flavor] = sales    # yearly_sales == {"vanila": [8580.0, 7201.25, 8900.0], ...}

# Print the dictionary of lists in tabular format
row_sum = 0
COLUMNS = 3    # number of columns
column_sum = [0] * COLUMNS

for flavor in sorted(yearly_sales):
    # Display the name of flavor
    print("%-15s" % flavor, end="")    # vanila
    
    # Display the sales associated with the flavor
    for i in range(COLUMNS): print("%10.2f" % yearly_sales[flavor][i], end="")    # 8580.0  7201.25  8900.0
    
    # Calculate and Display the sum of the sales having the flavor in common (i.e. row sum)
    row_sum = sum(yearly_sales[flavor])
    print("%15.2f" % row_sum)    # 24681.0 (== 8580.0 + 7201.25 + 8900.0)
    
    # Add sales each corresponding columns
    for i in range(COLUMNS): column_sum[i] += yearly_sales[flavor][i]

# Display the sum of each columns
print("               ", end="")
for total in column_sum: print("%10.2f" % total, end="")
print()

# Close the text file
file.close()
