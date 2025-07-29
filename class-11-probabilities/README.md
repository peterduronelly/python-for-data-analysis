# Modelling Probabilities

## Motivation

The lecture is related to the chapter that discusses probability models: regressions with binary y variables. In a sense, we can treat a binary $y$ variable just like any other variable and use regression analysis as we would otherwise. with a binary y variable, we can estimate nonlinear probability models instead of the linear ones. Data analysts need to have a good understanding of when to use these different probability models, and how to interpret and evaluate their results.

We start with linear probability models with multiple explanatory variables. We check the predicted outcome probabilities for certain groups. Then we focus on non-linear binary models: the logit and probit model. We estimate marginal effects, to interpret the average (marginal) effects of variables on the outcome probabilities. We overview goodness of fit statistics ($R^2$, Pseudo-$R^2$, Brier score, and Log-loss) along with visual and descriptive inspection of the predicted probabilities. Finally, we calculate the estimated bias and the calibration curve to understand model perform better.

## This lecture

- building and interpreting linear probability model, logit and probit models
- `patsy` package for creating design matrices with categorical variables, transofrmed variables and linear constrants
- comparing regression results using *calibration curves*
- plotting potential non-linear relationships between the expanatory variables and the binary outcome variable using `seaborn`
- accessing and visualizing key goodness-of-fit metrics

## Learning outcomes

After successfully completing the learning material, students will be familiar with

- carry out data transformations and feature engineering with the `patsy` package
- building probability models and assessing their absolute and relative performance
- calculating marginal effects for logit and probit regressions
- the sesntivity of the tails of the calibration curve to the probability bins