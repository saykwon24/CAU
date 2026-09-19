"""
Underfitting: a model that can neither model the training data nor generlize to new data
              model overlooks underlying patterns
Overfitting: a model that fits the training data too well, including details and noise
             negative impact on the model's ability to generalize
-> so carefully analyze the model's outputs to evaluate whether they are meeting the goals


Splitting Data: to prevent overfitting, split the data into some to train the model, and some to test the model
    1) Holdout: data is divided into train-validation-test sets (usually 60:20:20)
        model learns from training set, is tested on validation set
        if the performance is good enough, the model is tested on test set
        validation and test sets should come from the same distribution, something that reflects future data
    
    2) Cross-validation: data is divided into 'k' number of sets(k-folds)
        one set for testing, remainder(k-1 sets) for training
        repeat for all combinations of sets, then compute an average in each test


Classification Models: predict a class for each input, and output is commonly the probability of an input belonging to a class
                       can change the decision threshold
    1) Binary classification: the picture is a cat or not
    2) Multi-class: the picture is a cat, a dog, or an owl
    3) Multi-label: object in picture is a cat, an animal, and black


Confusion Matrix for Binary Classification: used to calculate evaluation metrics
    |                     | Predicted class positive | Predicted class negative |
    |---------------------+--------------------------+--------------------------|
    | True class positive |    True Positive(TP)     |    False Negative(FN)    |
    | True class negative |    False Positive(FP)    |    True Negative(TN)     |
        
        - True Positive(TP): actual == positive, predicted == positive
        - True Negative(TN): actual == negative, predicted == negative
        - False Positive(FP): actual == positive, predicted == negative
        - False Negative(FN): actual == negative, predicted == positive
    
    for multi-class settings, make a confusion table for each class, and then calculate average per class accuracy(balanced accuracy)
    it is useful when the data is unbalanced


Classification Model Evaluation
    1) overall accuracy == (TP + TN) / (TP + TN + FP + FN)
        of all events, how many were correct predictions(trues)?
        not informative when the class distribution is unbalanced
    
    2) Precision == TP / (TP + FP)
        of all positive predictions, how many were actually positive?
    
    3) Recall == TP / (TP + FN)
        of all actual positive results, how many did the model predict were positive?
    
    4) F1 Score == 2 * (Precision * Recall) / (Precision + Recall)
        compromise on precision and recall using the harmonic mean


Ensemble Learning: create a string model from an ensemble of weak models to improve the accuracy
                   the less correlation among base learners, the better
                   common for base learners to have different architectures


Scikit-Learn: pyton library that is most useful for ML and statistical modeling; regression, classification, and so on
              built upon NumPy, SciPy and Matplotlib
              follows 3-clause BSD license
              
              the basic supervised learning setup: feature matrix, target array
                (1) feature matrix: rows are instances, columns are features
                (2) target array: an array containing the training labels for each instance(row)
             
             Step 1) Set up feature matrix and target array
             Step 2) Choose model classes and Set model parameters
                Estimator: interface for building and fitting models -> Scikit-Learn
                Predictor: interface for making predictions
                Transformer: interface for converting data
             Step 3) Fit the model to data
             Step 4) Apply the model to new data
"""