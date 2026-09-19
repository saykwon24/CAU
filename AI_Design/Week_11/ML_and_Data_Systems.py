"""
Project Considerations for ML
    1) Framing the problem: defining the problem you want to solve with ML
        e.g. regression or classification -> binary or multiclass or multilable -> ...
            multiclass: a label acan belong to only one class
            multilabel: a lable can belong to multiple classes
    
    2) Objectives: specific goals and outcomes you aim to achieve
                   should be specified and corresponded with Framing
        (1) ML system objectives: improve performance, reduce latency
        (2) Business objectives: improve ROI(Return on Investment), reduce cost, follow regulation and compilance
        comparing ML and business objectives can be tricky, so 'mapping' is important
            - Baseline(기준점)
            - Usefulness Threshold(유의미한 기준)
            - False Positive vs. False Negative; will the wrong prediction be regarded good or bad?
            - Interpretability(해석 가능성)
            - Confidence Measurement(신뢰도 측정)
    
    3) Constraints: limitations or restrictions that can affect how you approach and execute the project
        time vs. budget (time/budget tradeoffs), privacy
            time: rule of thumb = 20% time to get initial working system, 80% on iterative development
            budget: data, resources, talent, and so on
        privacy: shipping data for annotation, how long and what kind of data can be stored, sharing 3rd-party solutions, conforming regulations
    
    4) Phases: each process steps for ML adoption
        (1) Before ML
            decoupling different objectives - easier for training and maintenance, easier to tweak your system
        (2) Simplest ML models: start with a simple model with which validate hypothesis and pipeline
        (3) Optimizing simple models
            one model optimizes combined loss
            multiple objective optimization(MOO): each model optimizes one objective
        (4) Adopting complex ML models


Data Engineering: data sources, formats, models, storage or engines, and processing
    1) Data Sources: where you data is coming from
        users generated data   | easily mal-formatted, so need to be processed ASAP (e.g. users behavioral data)
        systems generated data | easier to standardize, OK to precess periodically
                                 can grow very large and quickly, OK to delete when no longer useful

    2) Data Formats: various formats such as structured, semi-structured, or unstructured and means how to store your data
        storing your data is only interesting if you want to access it later
        data formats are agreed upon standards to serialize your data so that it can be transmitted and reconstructed later
            storing data - serialization
            unloading data - deserialization
        row-major    | stored and retrieved row-by-row
                       good for accessing samples (e.g. CSV, Numpy ndarray)
        column-major | stored and retrieved column-by-column
                       good for accessing features (e.g. Parquet, Pandas DataFrame)

    3) Data Models: defining the structure and relationships wihin your data
    
    4) Data Storage(Engines): systems or databases used to store and manage data
    
    5) Data Processing: transforming and preparing data for ML
"""