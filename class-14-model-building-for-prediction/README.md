# Model-building Using `Lasso`

## Motivation

In this lecture is our first venture into machine learning! We introduce `lasso` (Least Absolute Shrinkage and Selection Operator), a technique which helps us pick the important explanatory variables in a linear regression from as many as hundrends of possible ones! In one of the exercises we develop a technique to reduce the potential 370 x-variables to a handful. 

We also introduce the conecept of `grid search` where we try out various options for an important model parameter and let the computer select the right one based on the performance of our moodel. We split our data to train and test subsets, build the model on the train set and test model performance on the training set to avoid overfitting our model to the training data.

## This lecture

- EDA using `matplotlin` and `seaborn`
- splitting data into traind and test subsets using the `scikit-learn` library
- creating cross-validation workflows using `sklearn`
- `lasso` doing the hard way and using `grid search`
- complex model diagnostics, prediction intervals 

## Learning outcomes

After successfully completing the learning material, students will be familiar with

- the main concepts in `lasso`
- grid search and cross-validation
- using the computer'a brute computing force for model selection