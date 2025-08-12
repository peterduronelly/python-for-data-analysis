# Probabilities And Classification

## Motivation

Here we extend our modelling toolkit to build models for predicting the values of binary variables. These variables can take two values only, mostly modelled with 0 and 1, and our task it to assign a probability for this variable to have the value of 1. This is *probability* prediction. 

If we want to assign our observation to one of the possible outcome of this binary variable we talk about *classification*. 

We start with developing multiple models to predict probabilities and learn how to measure these models' performance. We then discuss to do classifaction using the predicted probabilities by applying various thresholds, and explore the metrics to find the this best threshold. 

## This lecture

- linear probability models using OLS, logit and lasso
- cross-validation with the logit model
- model evaluation metrics and methods: calibration curve, confusion matrix, ROC and AUC
- model comparison using RMSE and AUC
- user-defned loss functions
- modelling probabilities using tree-based methods (CART & random forest)

## Learning outcomes

After successfully completing the learning material, students will be familiar with

- linear probability models and logit, and the difference between them
- interpreting OLS and logit model outputs
- how to get marginel effects of a logit regression
- the basics of optimization algorithm for cross-validation using a loss function
- how to get AUC values for probability predictions from the model outputs
- visualizing model perfomrance using the ROC curve
- calculating and interpreting the confusion matrix