import json


# Reading data from a JSON file
with open('input_large_inventory.json', 'r') as json_file:
    data = json.load(json_file)
data[0]


# Writing or Updating data in JSON format
data[0]['value'] = data[0]['quantity'] * data[0]['price']
data[0]

for i in range(len(data)):
    data[i]['value'] = data[i]['quantity'] * data[i]['price']
data


# Loading and Saving JSON format (in a new file)
with open('output.json', 'w') as json_file:
    json.dump(data, json_file)
