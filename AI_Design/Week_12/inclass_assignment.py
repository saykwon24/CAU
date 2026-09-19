import pandas as pd

## Data loading and missing value check
dataset = pd.read_csv("./Data.csv")
dataset.isnull().any()


## Handling missing values: fill them with mean for 'Age' column and median for 'Salary' column
dataset['Salary'].fillna(dataset['Salary'].mean(), inplace=True)
dataset['Age'].fillna(dataset['Age'].median(), inplace=True)
dataset.isnull().sum()
print(dataset)


## Feature engineering: create new feature column 'Salary_to_Age_Ratio'
dataset['Salary_to_Age_Ratio'] = dataset['Salary'] / dataset['Age']


## Categorical data encoding: apply one-hot encoding to 'Country' column and binary encoding to 'Purchased' column
dataset = pd.get_dummies(dataset, columns=['Country'])
dataset["Purchased"] = dataset["Purchased"].map({"No":0, "Yes":1})


## Scaling: apply min/man normalization to 'Age', 'Salary' and 'Salary_to_Age_Ratio'
dataset["Age"] = (dataset["Age"] - min(dataset['Age'])) / (max(dataset['Age']) - min(dataset['Age']))
dataset["Salary"] = (dataset["Salary"] - min(dataset['Salary'])) / (max(dataset['Salary']) - min(dataset['Salary']))
dataset["Salary_to_Age_Ratio"] = (dataset["Salary_to_Age_Ratio"] - min(dataset['Salary_to_Age_Ratio'])) / (max(dataset['Salary_to_Age_Ratio']) - min(dataset['Salary_to_Age_Ratio']))


## Final data check and save
dataset.head(5)

dataset.to_csv("processed_data_10-2.csv")