import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score


data = pd.read_csv('abalone.csv')

# for given features, predict whether the # of 'Rings' is higer than 10 or not
data = pd.get_dummies(data)
x_data = data.drop(["Rings"], axis=1)    # feature matrix
y_data = (data["Rings"] > 10)            # target array


# apply standard scaling for the dataset
scaler = StandardScaler()
scaler.fit(x_data)
x_data_norm = scaler.transform(x_data)


# separate the data into training and test sets
x_data_train, x_data_test, y_data_train, y_data_test = train_test_split(x_data, y_data, test_size=0.25, random_state=5)

# choose a model and parameters, and fit the model to data
for i in [3, 5, 7]:    # apply at least three 'k' (e.g. k == 3, 5, 7)
    knn = KNeighborsClassifier(n_neighbors=i)
    
    # fit the model to the training set
    knn.fit(x_data_train, y_data_train)
    
    # apply model to a new data
    y_data_test_model = knn.predict(x_data_test)

    # compute accuracy, balanced accuracy, and f1 score
    print(accuracy_score(y_data_test, y_data_test_model))
    print(f1_score(y_data_test, y_data_test_model, average='micro'))
    print(balanced_accuracy_score(y_data_test, y_data_test_model))
    print()