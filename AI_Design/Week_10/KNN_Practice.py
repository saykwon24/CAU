from sklearn import datasets
import math
import random

""" basics for KNN Practice """
# Data load
iris = datasets.load_iris()

# Data visulize
print(len(iris['data']))      # 150; # of data
print(set(iris['target']))    # {0, 1, 2}; three classes - Setosa, Versicolor, and Virginica
x = iris['data'][0]
print(x)                      # array([5.1, 3.5, 1.4, 0.2]); four features - sepal length and width, petal length and width
print()

# Data processing and exploring the data structure
dataset = [list(x) + [y] for x, y in zip(iris['data'], iris['target'])]
print(dataset[0])    # [5.1, 3.5, 1.4, 0.2, 0]; first four are Features(Input) and last one is Label(Target)
label_zero = len([x for x in dataset if x[-1] == 0])
print(label_zero)    # number of data points whose label is 0




""" 5 steps for KNN Practice """
# Combine features and label
dataset = [list(x) + [y] for x, y in zip(iris['data'], iris['target'])]

## Step 1) Calculate Euclidean Distance
# Function to calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    
    # Iterate over each feature, excluding the label
    for i in range(len(row1) - 1):
        ###############################################################
        distance += (row1[i] - row2[i])**2
        ###############################################################
    
    return math.sqrt(distance)



## Step 2) Get Nearest Neighbors
# Function to locate the most similar neighbors for a test row
def get_neighbors(train, test_row, num_neighbors):
    distances = []
    
    # Calculate the distance between the test row and each row in the training dataset
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    
    # Sort the list of distances in ascending order
    distances.sort(key=lambda tup: tup[1])
    
    ###############################################################
    # Select the top 'num_neighbors' rows based on the smallest distances
    neighbors = list()
    
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    ###############################################################
    
    return neighbors


# Function to make a prediction with neighbors
def predict_classification(train, test_row, num_neighbor):
    # Retrieve the nearest neighbors
    neighbors = get_neighbors(train, test_row, num_neighbor)
    
    ###############################################################
    # Extract the label of each neighbor
    output_values = [neighbor[0] for neighbor in neighbors]
    ###############################################################
    
    # Return the most common class label among neighbors
    prediction = max(set(output_values), key=output_values.count)
    
    return prediction


# K-NN algorithm
def k_nearest_neighbors(train, test_row, num_neighbors):
    return predict_classification(train, test_row, num_neighbors)



## Step 3) Make Predictions
# Cross-Validation: split the data into n_folds, evaluate the K-NN classifier on each fold, and then calculate the mean accuracy over all folds
# (1) Split a dataset into k folds for cross-validation
def cross_validation_split(dataset, n_folds):
    dataset_split = []
    dataset_copy = list(dataset)
    fold_size = len(dataset) // n_folds
    
    # Create folds by randomly sampling data
    for _ in range(n_folds):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        
        dataset_split.append(fold)
    
    return dataset_split


# (2) Evaluate an algorithm using cross-validation
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = []
    
    # Run the algorithm on each fold
    for fold in folds:
        train_set = [row for sublist in folds if sublist != fold for row in sublist]     # All data except the fold
        test_set = [list(row) for row in fold]
        
        # Set the lable to None to separate prediction from original
        for row in test_set: row[-1] = None
        
        # Get predictions
        predicted = [algorithm(train_set, row, *args) for row in test_set]
        
        # Extract actual labels for comparison
        actual = [row[-1] for row in fold]
        
        # Calculate accuracy
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
        
    return scores

# Calculate accuracy percentage(%)
def accuracy_metric(actual, predicted):
    correct = sum(1 for i in range(len(actual)) if actual[i] == predicted[i])
    return correct / len(actual) * 100


# (3) Evaluate the result
# Seed the random number generator for reproducibility
random.seed(1)

# Evaluate K-NN on the Iris dataset
n_folds = 5
num_neighbors = 5
scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)

# Print out scores and mean accuracy
print("Scores:", scores)
print("Mean Accuracy:", sum(scores) / len(scores))