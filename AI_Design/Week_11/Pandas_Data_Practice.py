import pandas as pd


## Exercise: Loading CSV file, Concatenating objects, and then writing dataframe to Excel
# Load dataset in CSV file and Make a dataframe
df = pd.read_csv('iris.csv')
df

# Slice or Pick first and last 5 rows to make a new dataframe (list)
pieces = [df[:5], df[-5:]]
pieces

# Concatenate objects to make dataframe
new_df = pd.concat(pieces)
new_df

# Writing dataframe to excel
new_df.to_excel('new_df.xlsx', sheet_name="sheet1")
pd.read_excel('new_df.xlsx')