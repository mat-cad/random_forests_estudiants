
# Random Forest object oriented

![](bosc_montseny.jpeg)

This practicum is about building a modular and extensible object-oriented design and implementation in Python of random forests. This was a popular and effective method for classification and regression in machine learning before this field was taken by storm by deep neural networks. Nowadays it is still a good solution for problems where one can easily handcraft *features*. 

This practicum was done for the Object Oriented Programming course of the Matemàtiques Computacionals i Anàlisi de Dades (Mad-CAD), Universitat Autònoma de Barcelona, 2020-21. Handout is available in [Overleaf](https://www.overleaf.com/read/dfjyxpnybjgp).

The goal was to learn object oriented design and programming in Python plus coding style, logging and, along the way, the basics of machine learning.

<!---
replace link to overleaf by pdf
--->


## Requirements

- Python 3.x
- Numpy
- Matplotlib
- Logging

## Usage

Follows scikit-learn style

```python
# 
rf = RandomForestClassifier(
        max_depth,    # of each decision tree
        min_size,     # of a node to make it a leave
        ratio_sample, # to get the size of the dataset when looking for the best split
        n_trees,      # number of trees in the forest
        n_features,   # number of features (randomly selected) to consider when looking for the best split 
        criterion     # either Gini or Entropy              
)
rf.fit(Xtrain, ytrain)
ypred = rf.predict(Xtest)
# and same for regression
rf = RandomForestRegressor(...)
```

## Authors

This is team work with Pere Garriga and Genis Soler.

<!---
maybe link to their Github accounts 
-->


