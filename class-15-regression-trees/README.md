# Regression Trees

## Motivation

This lecture introduces the regression tree, an alternative to linear regression for prediction purposes that can find the most important predictor variables and their interactions and can approximate any functional form automatically. Regression trees split the data into small bins (subsamples) by the value of the x variables. For a quantitative y, they use the average y value in those small sets to predict y. We introduce the regression tree model and the most widely used algorithm to build a regression tree model. 

Classification and regression trees (CART) are not used for modelling or prediction in a standalone fashion, but rather as the major building block for most complex algorithms. We, however, spend a whole class on these models to understand these basics later in our studies. 

## This lecture

- estimating and visualizing regression trees
- stopping criteria for CART: depth, number of leaves and minimum marginal improvement in fit
- pruning large trees
- plotting and interpreting variable importances, building OLS models using the insight from CART feature importances

## Learning outcomes

After successfully completing the learning material, students will be familiar with

- how classification and regression trees work
- how to build regression trees with the `scikit-learn` library
- plotting CART predictions
- how to implement various stopping criteria for model building