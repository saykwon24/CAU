import pandas as pd
import numpy as np


# Create a DataFrame
dates = pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
print(df)
print()

# Selection by label
print(df["A"])
print(df.loc[dates[0]])
print(df.loc[:, ["A", "B"]])
print()

# Slicing
print(df[0:3])
print(df['20130102':'20130104'])
print()

# Selection by position
print(df.iloc[3])
print(df.iloc[3:5, 0:2])
print()

# Entries Filtering
print(df > 0)
print(df[df['A'] > 0])
print(df.drop('20130103'))
print()

# Concatenating Objects(DataFrames)
df = pd.DataFrame(np.random.rand(10, 4))
print(df)
print()

pieces = [df[:3], df[3:7], df[7:]]
df_concat = pd.concat(pieces)
print(df_concat)
print()