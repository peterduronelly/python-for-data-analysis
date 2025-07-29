# Multiple Linear Regression 

## Motivation

After understanding simple linear regression, we can turn to multiple linear regression, which has more than one explanatory variable. Multiple linear regression is the most used method to uncover patterns of associations between variables. There are multiple reasons to include more explanatory variables in a regression. We may be interested in uncovering patterns of association between y and other explanatory variables, which may help us understand differences in terms of the x variable we are interested in most. Or, we may be interested in the effect of an x variable, but we want to compare observations that are different in x but similar in other variables. Finally, we may want to predict y, and we want to use more x variables to arrive at better predictions.

## This lecture

- running multiple regressions using the `statsmodels` package
- comparing regression results
- accessing the key metrics from our regression results
- plotting regression results using `matplotlib` and `seaborn`

## Learning outcomes

After successfully completing the learning material, students will be familiar with

- visualizing multiple explanatory variables with the outcome
- using `statsmodels` to estimate, `stargazer` to summarize multiple linear regressions
- simplify complex regression outputs for more compact presentation