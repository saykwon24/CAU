import pandas as pd


# Define some data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age' : [24, 27, 22],
    'City': ['New York', 'San Fancisco', 'Los Angeles']
}

# Create and Display the dataframe
df = pd.DataFrame(data)
print(df)
print()

# Print first 2 rows in 'data'
df.head(2)
# Print last 2 rows in 'data'
df.tail(2)

# Filter 'DataFrame' to include specific condition
df_filtered = df[df['Age'] > 23]
print(df_filtered)
print()

# Print average of 'Age' datas of the filtered datas
print(float(df_filtered['Age'].mean()))    # use float() function to display only the number
print()

# Aggregate data by city and calculate the average age
df_aggregate = df.groupby('City')['Age'].mean()
print(df_aggregate)
print()

# Create a new column that indicates whether the person is of legal age or underage
df['Adult'] = df['Age'].apply(lambda x: 'Yes' if x >= 18 else 'No')

# Delete the Age column
df_output = df.drop(columns=['Age'])
print(df_output)
print()

# Save Dataframe to a CSV file
df_output.to_csv('people.csv', index=False)