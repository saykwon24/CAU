"""
Machine Learning: statistical algorithms that can effectively generalize and thus perform tasks 'without' explicit instructions
                  categories: supervised, unsupervised, and reinforcement learning


Supervised Learning: learns from 'labeled' training data to make predictions or decisions without human intervention
                     is often used to map input data and output label
                     an objective is to minimize the loss
    1) Classification | assign input data points to predefined categories or classes
    2) Regression     | predict a continuous numerical value or quatity

Unsupervised Learning: trained on 'unlabeled' data without any predefined target or output label
                       its goal is to find patterns, structures, or relationships within the data
    1) Clustering                            | group similar data points based on similarities
    2) Dimensionality Reduction(Compression) | reduce the number of features or variables while preserving its essential information

Reinforcement Learning: focuses on training algorithms to make sequences of decisions by 'interacting with an environment'
                        there is an 'reward' system that is numerical signal about the action
                        learning by 'doing' with delayed reward
                        an objective is to maximize the reward or expected result


Some ML Terminology
    Training example    | a 'row' in the table representing the dataset (also called training sample)
    Feature             | a 'column' in the table representing the dataset
    Targets             | what we want to predict (also called ground truth or label)
    Output / Prediction | output from the model, which distinguish from targets
    Loss Funciton       | function that measures the difference between estimates and actual target values


5 steps for ML application
    1) Define the problem to be solved; goals, specific task, and precise problem
    2) Collect (labeled) data; quality and quantity of the data can significantly impact performance
    3) Choose an algorithm class; depending on the type of the problem
    4) Choose an optimization metric or measure for learning the model
    5) Choose a metric or measure for evaluating the model; assess the quality of generalization for unseen data


K-Nearest Neighbor(K-NN): find K nearest data labels from a new data point
    1) Calculate Euclidean Distance
    2) Get Nearest Neighbors
    3) Make Predictions
"""
