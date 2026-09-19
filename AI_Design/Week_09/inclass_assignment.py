#1) Data setup: create a dictionary and convert it into a pandas DataFrame
import pandas as pd

data = {
    'Date': ['2024-10-01', '2024-10-01', '2024-10-02', '2024-10-02', '2024-10-03', '2024-10-03'], 
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [150, 200, 180, 220, 170, 210]
}

df = pd.DataFrame(data)
print(df)
print("\n")



#2) Data Manipulation: calculate total sales for each and average daily sales for each
total = [df[df['Product'] == 'A']['Sales'], df[df['Product'] == 'B']['Sales']]

print("Total Sales for Product A:", int(total[0].sum()))
print("Total Sales for Product B:", int(total[1].sum()))

print("Average Sales for Product A %.2f" % float(total[0].mean()))
print("Average Sales for Product B %.2f" % float(total[1].mean()))
print("\n")



#3) Visualization: Create a line plot and a bar plot
import matplotlib.pyplot as plt

x = ['2024-10-01', '2024-10-02', '2024-10-03']
A = [data['Sales'][0], data['Sales'][2], data['Sales'][4]]    # [150, 180, 170]
B = [data['Sales'][1], data['Sales'][3], data['Sales'][5]]    # [200, 220, 210]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

# first subplot
ax1.plot(x, A, marker='o', color='blue', label='A', linewidth=2)
ax1.plot(x, B, marker='o', color='orange', label='B', linewidth=2)
ax1.set_title('Daily Sales Trend by Product')
ax1.legend(title='Product')

# second subplot
ax2.bar(['A', 'B'], [int(total[0].sum()), int(total[1].sum())], color='blue')
ax2.set_title('Total Sales by Product')

plt.tight_layout()
plt.show()