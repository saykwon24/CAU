import pandas as pd
import json


## Loading JSON file
with open('input_large_inventory.json', 'r') as json_file:
    data = json.load(json_file)


## Data Enhancement
for i in range(len(data)):
    data[i]['total_value'] = data[i]['quantity'] * data[i]['price']


## Data Preparation for Machine Learning
#1) Normalize using min-max normalization
prices = [x['price'] for x in data]
for i in range(len(data)):
    data[i]['norm_price'] = (data[i]['price'] - min(prices)) / (max(prices) - min(prices))

#2) Encode the demand_label using binary encoding
for i in range(len(data)):
  # high to 1 and low to 0
    if data[i]['demand_label'] == 'low':
        data[i]['demand_label'] = 0
    else:
        data[i]['demand_label'] = 1

with open('new_inven.json', 'w') as f:
    json.dump(data, f)

#3) Filter out items with a quantity of greater than 10
df = pd.read_json("new_inven.json")
df = df[df['quantity'] >= 10]


## Data Analysis and Summary
df[df['demand_label'] == 1]['total_value'].mean()
print(len(df[df['demand_label'] == 0]), len(df[df['demand_label'] == 1]))


## Update and Save data to CSV format
df.to_csv("assignment.csv")