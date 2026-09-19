"""
Iris dataset: a rite of passage for applying ML
              contains 150 instance, 4 features, and 3 classes(labels)
"""

## Step 1) Iris Feature Matrix and Target Array
import pandas as pd

iris = pd.read_csv('iris.csv')
x_iris = iris.drop("variety", axis=1)    # feature matrix x: input
y_iris = iris["variety"]                 # target array y: output

# check the number of samples in feature matrix x == number of labels in target array y
x_iris.shape[0] == y_iris.shape[0]    # True; 150 samples and 150 target labels


## Step 2) Choose a Model and Parameters
from sklearn.neighbors import KNeighborsClassifier

n_neighbors = 3
knn = KNeighborsClassifier(n_neighbors=n_neighbors)


## Step 3) Fit Model to Data
from sklearn.model_selection import train_test_split

# separate the data into non-overlapping trainig and test subsets
x_iris_train, x_iris_test, y_iris_train, y_iris_test = train_test_split(x_iris, y_iris, test_size=0.25, random_state = 5)
print("# Num of train", len(x_iris_train))
print("# Num of test", len(x_iris_test))

# fit the model to the training data
knn.fit(x_iris_train, y_iris_train)


## Step 4) Apply Model to New Data
y_iris_test_model = knn.predict(x_iris_test)



## Exercise 1: compare the results using only two features, 'sepal.length' and 'petal.length'
x_iris_train_length = x_iris_train.drop(["sepal.width", "petal.width"], axis=1)
x_iris_test_length = x_iris_train.drop(["sepal.width", "petal.width"], axis=1)
x_iris_train_length


## Exercise 2: scaling or normalization to the data, and then experiment(fit) again
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(x_iris)
x_iris_norm = scaler.transform(x_iris)


## Exercise 3: calculate accuracy, balanced accuracy, and f1 score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import balanced_accuracy_score

print(accuracy_score(y_iris_test, y_iris_test_model))
print(f1_score(y_iris_test, y_iris_test_model, average='micro'))
print(balanced_accuracy_score(y_iris_test, y_iris_test_model))