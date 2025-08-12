# Random Forest And Boosting

## Motivation

This is machine learning in action! We introduce two so-called ensemble methods: random forest and boosting. The first method, `random forest` combines $n$ independent trees, each making incacurate predictions, but combining these *weak learners* and averaging out their individual results we can come up with more precise forecasts.

`Boosting`, on the other hand, starts with a random tree and builds other trees on top of this initial tree on a sequential basis, focusing on data points where the mispredictions are the largest. 

This is a very demanding class where we cover a many steps of building an ensemble model. 

## This lecture

- estimating a random forest model with `sklearn`
- understand `max_features` and `min_sample_split` parameters
- hyperparameter tuning with cross validation using `GridSearchCV`
- variable importance for standalone and grouped variables
- partial dependence plots and sub-sample analysis
- SHAP values
- `GBM` and `LightGBM` models
- building pipelines for repeated model building and built-in hyperparameter tuning
- comparing model performances across model families

## Learning outcomes

After successfully completing the learning material, students will be familiar with

- building random forest models and analyzing their output
- building boosting algorithms
- creating a complex workflow for model building and selection