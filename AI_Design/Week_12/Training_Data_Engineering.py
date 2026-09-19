"""
Labeling: assigning meaningful and descriptive categories to data points
    1) Hand-labeling: by human annotators
    
    2) Programmatic labeling: by automated algorithms
    
    3) Weak Supervision: Leverage noisy, imprecise sources to create labels
                         a small number of labels is useful to guide the development of heuristics
    
    4) Semi-supervision: combines both labeled and unlabeled data to improve the performance
                         structural assumption: small perturbation wouldn't change a sample's label
                         a small number of initial labels(ground truths) as seeds to generate more labels
        (1) Train model on a small set of labeled data
        (2) Use this model to generate predictions for unlabeled data
        (3) Use predictions with high raw probabilities as labels
        (4) Repeat (1) with new labeled data

    5) Active Learning: improves the efficiency of labeling data by selecting and labeling the 'most valuable' data samples
                        ground truth is required
        Metrics for label samples: uncertainty(or confidence) measurement, candidate models' disagreement


Feature Engineering: create a new features or modify existing ones to improve ML models
                     Engineered Features: features that is created or modified through feature engineering
    
    1) Handling missing values: deletion, imputation
        kinds of missing value: not all missing values are equal
            Missing Not At Random(MNAR)        | related to missing values themselves
            Missing At Random(MAR)             | related to some other observed variables
            Missing Completely At Random(MCAR) | unrelated to any other variable, no pattern, do not introduce bias
        (1) Deletion
            column deletion: remove columns with too many missing entries
                             but the remaining data still potentially useful
            row deletion: good for MCAR, bad for MNAR and MAR
                          bad when there are many missing fields
        (2) Imputation: fill missing fields with certain values (e.g. statistical measures; mean, median, mode)
                        default is to fill with '0' or 'empty string'
    
    2) Scalig: process of transforming numerical feature to a similar range
        (1) min/max normalization: x' = (x - min(x)) / (max(x) - min(x))
        (2) z-score normalization: when variables follow a normal distribution
        (3) log scaling: when variables follow an exponenetial distribution
    
    3) Discretization(or Quantization): converting continuous numerical features into discrete bins or categories
                                        create buckets for different ranges
    
    4) Encoding Categorical features: discrete variables such as gender, color, or city
                                      represent each category with its attribute, and then use hash function to hash categories to different indices (hashing trich)
        One-hot Encoding: represent categorical variables as binary vectors with all zero values except for the index that corresponds to the category, which is marked with a 1
"""