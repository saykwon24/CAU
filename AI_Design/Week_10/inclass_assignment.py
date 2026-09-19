from sklearn import datasets
import matplotlib.pyplot as plt
import random
import math

digits = datasets.load_digits()

plt.gray()
plt.matshow(digits.images[0])
plt.show()

dataset = [list(x) + [y] for x, y in zip(digits.data, digits.target)]


## Step 1) Calculate Euclidean Distance
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i])**2
    
    return math.sqrt(distance)



## Step 2) Get Nearest Neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = []
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    
    distances.sort(key=lambda tup: tup[1])
    neighbors = list(distances[:num_neighbors])
    
    return neighbors


def predict_classification(train, test_row, num_neighbor):
    neighbors = get_neighbors(train, test_row, num_neighbor)
    output_values = [neighbor[0][-1] for neighbor in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    
    return prediction


def k_nearest_neighbors(train, test_row, num_neighbors):
    return predict_classification(train, test_row, num_neighbors)



## Step 3) Make Predictions
def cross_validation_split(dataset, n_folds):
    dataset_split = []
    dataset_copy = list(dataset)
    fold_size = len(dataset) // n_folds
    
    for _ in range(n_folds):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    
    return dataset_split


def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = []
    
    for fold in folds:
        train_set = [row for sublist in folds if sublist != fold for row in sublist]
        test_set = [list(row) for row in fold]
        for row in test_set: row[-1] = None
        predicted = [algorithm(train_set, row, *args) for row in test_set]
        actual = [row[-1] for row in fold]
        
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
        
    return scores


def accuracy_metric(actual, predicted):
    correct = sum(1 for i in range(len(actual)) if actual[i] == predicted[i])
    return correct / len(actual) * 100


# Seed the random number generator for reproducibility
random.seed(10000)

# Evaluate K-NN on the Iris dataset
n_folds = 3
num_neighbors = 5
scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)

# Print out scores and mean accuracy
print("Scores:", scores)
print("Mean Accuracy:", sum(scores) / len(scores))