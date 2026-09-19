"""
Matplotlib: graphical plotting library for Python, open source
            license is based of Python Software Foundation(PSF) license: non-profit corporation
            uses shared, collective copyright model
            two APIs: pyplot API, Object-Oriented API collection of objects
>>> https://matplotlib.org/cheatsheets/
"""

import matplotlib.pyplot as plt
import numpy as np


## Example 1: Customize marker & linestyle
xaxis = np.array([2, 12, 3, 9])
plt.plot(xaxis, marker='o', linestyle='--')
    # because y axis is not defined, vertical axis is 'xaxis'
plt.show()



## Example 2: Line Plot
x = np.linspace(0, 10, 100)    # divide a range between 0 and 10 into 100 elements
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Sine Wave', color='blue', linewidth=2)    # label: 범례 이름
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave Plot')
plt.legend()
plt.grid(True)
plt.show()



## Exercise 3: Line Plot
x = [2018, 2019, 2020, 2021, 2022]
y = [50, 65, 80, 90, 105]

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', color='orange', linewidth=2)
plt.title('Company Revenue Growth Over Years')
plt.xlabel('Year')
plt.ylabel('Revenue (Millions)')
plt.grid(True)
plt.show()



## Example 4: Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 8, 2, 6]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='green')    # use 'plt.bar' to draw a bar chart
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y')
plt.show()



## Exercise 5: Bar Plot
Quarters = ["Q1", "Q2", "Q3", "Q4"]
Product_sold = [150, 200, 250, 300]

plt.figure(figsize=(10, 6))
plt.bar(Quarters, Product_sold, color='skyblue')
plt.title('Quarterly Product Sales')
plt.xlabel('Quarter')
plt.ylabel('Product Sold')
plt.grid()
plt.show()



## Example 6: Scatter Plot
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.title('Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.colorbar()    # in the right side of the plot
plt.show()