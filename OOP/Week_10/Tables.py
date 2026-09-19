# Week 10 (1)
"""
Table: Python does not have a data type for table, but can be created using list (list in list)
       rows are elements of external list, columns are element of internal list
       first, create a list that stores the individual rows,
       then create a new list using replication for each row in the table and append it to the list of rows
       can access individual elements in a table by using index: 'table[i][j]'
       
       when you pass a table to a function, you should recover the dimensions
       1) number of rows == len(table)
       2) number of columns == len(table[0]), len(table[1]), or ...
"""

## Create a table that has 5 rows and 20 columns
ROWS = 5
COLUMNS = 20

table = []
for i in range(ROWS):
    row = [0] * COLUMNS
    table.append(row)


## Access all elements of table by using nested loops
COUNTRIES = 8
MEDALS = 3
counts = [
    [ 0, 3, 0 ],
    [ 0, 0, 1 ],
    [ 0, 0, 1 ],
    [ 1, 0, 0 ],
    [ 0, 0, 1 ],
    [ 3, 1, 1 ],
    [ 0, 1, 0 ],
    [ 1, 0, 1 ]
]

for i in range(COUNTRIES):
    for j in range(MEDALS):
        print("%8d" % counts[i][j], end="")
        print()    # new line


## Locating Neighboring Elements: be careful at the boundary of the list
total = 0
if i > 0: total += counts[i - 1][j]           # check top boundary
if i < ROWS - 1: total += counts[i + 1][j]    # check bottom boundary


## Computing row and column totals
total = 0
for i in range(COUNTRIES):
    for j in range(MEDALS): total += counts[i][j]    # row totals
    print(total)
    total = 0

for j in range(MEDALS):
    for i in range(COUNTRIES): total += counts[i][j]    # column totals
    print(total)
    total = 0


## Using tables with functions
def sum(values):
    total = 0
    for i in range(len(values)):
        for j in range(len(values[0])): total += values[i][j]
    return total


## Table with variable row lengths
b = []
for i in range(3): b.append([0] * (i + 1))    # lower triangular matrix form
    # number of rows == len(b)
    # length of the i-th row == len(b[i])

#1) Traverse all elements of table with list index
for i in range(len(b)):
    for j in range(len(b[i])): print(b[i][j], end="")
    print()

#2) Traverse all elements of table without list index
for row in b:
    for element in row: print(element, end="")
    print()