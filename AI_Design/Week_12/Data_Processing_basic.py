import pandas as pd

# Import the dataset
dataset = pd.read_csv("./Data.csv")

# Identify missing values in the dataset
dataset.isnull()

# Identify missing values per column
dataset.isnull().any()    # axis=0 by default
dataset.isnull().any(axis=1)  # row


## Exercise 1: fill the missing values with mean value
dataset['Salary'].fillna(dataset['Salary'].mean(), inplace=True)
dataset['Age'].fillna(dataset['Age'].mean(), inplace=True)
dataset


## Exercise 2: apply one-hot encoding to 'Country' column
dataset = pd.get_dummies(dataset, columns=['Country'])
dataset["Country_France"] = dataset["Country_France"].map({False:0, True:1})
dataset["Country_Germany"] = dataset["Country_Germany"].map({False:0, True:1})
dataset["Country_Spain"] = dataset["Country_Spain"].map({False:0, True:1})
dataset


## Exercise 3: apply min-max normalization to numerical columns 'Age' and 'Salary'
dataset["Age"] = (dataset["Age"] - min(dataset['Age'])) / (max(dataset['Age']) - min(dataset['Age']))
dataset["Salary"] = (dataset["Salary"] - min(dataset['Salary'])) / (max(dataset['Salary']) - min(dataset['Salary']))
dataset