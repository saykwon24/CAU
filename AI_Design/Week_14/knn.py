"""
in-class assignment
    1) use "anaconda prompt"
    2) copy the address of 'knn.py' and enter "cd address" in command line
    3) enter "streamlit run knn.py" in command line
    
    "Ctrl + C" to stop the running of app.py
"""


import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import balanced_accuracy_score


#############################################
## 1) Change the title
st.title("In-Class Assignment")
#############################################

iris = pd.read_csv("iris.csv")

X_iris = iris.drop("variety", axis=1)
X_iris = X_iris.drop("sepal.width", axis=1)
X_iris = X_iris.drop("petal.width", axis=1)
y_iris = iris['variety']

#############################################
## 2) Hyperparameter Tuning: add slider
st.header("Hyperparameter Tuning")
n_neighbors_ = st.slider('Select number of neihghbors (k)', 1, 15, 3)
st.write("K is", n_neighbors_)
#############################################

X_iris_train, X_iris_test, y_iris_train, y_iris_test = train_test_split(X_iris, y_iris, random_state=1)

knn = KNeighborsClassifier(n_neighbors=n_neighbors_)
knn.fit(X_iris_train, y_iris_train)
y_iris_test_model = knn.predict(X_iris_test)

acc = round(accuracy_score(y_iris_test, y_iris_test_model), 2)
bal_acc = round(balanced_accuracy_score(y_iris_test, y_iris_test_model), 2)

print("Balanced accuracy for the test set: ", bal_acc)

#############################################
## 3) Dynamic Performance Evaluation: retrain this KNN model and then recalculate and display the model's accuracy and balanced accuracy
st.header("Model Performance")
st.write("Model Accuracy:", acc)
st.write("Balanced Accuracy:", bal_acc)
#############################################

st.header("Iris Species Classifier")
user_text = st.text_input("Enter the sepal.length and petal.length for the iris. Please enter in the form of a,b.")
    
try:
    sl,pl = user_text.split(',')
    sl = float(sl)
    pl = float(pl)

    new_test_raw_data = {'sepal.length':[sl], 'petal.length':[pl]}
    new_test_data = pd.DataFrame(new_test_raw_data) 

    prediction = knn.predict(new_test_data)
    st.write("Predicted Label: ", prediction[0])
except:    
    st.write("You entered invalid input. Please enter the correct value")
