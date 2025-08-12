# Time Series Predictions

## Motivation

This lecture discusses forecasting: prediction from time series data for one or more time periods in the future. The focus of this chapter is forecasting future values of one variable, by making use of past values of the same variable, and possibly other variables, too.  

The first lecture is about *deterministic* time series models where the $y$ variable changes by time and this change follows a recognizable pattern consisting of a trend and some seasonal factors. We use linear regression to account for the effect of the underlying trend and these seasonal factors first, then we explore Meta's `Prophet` model which decomposes time series data into these factors on the fly. 

The second lecture covers *stochastic* modelling where the ubderlying $y$ variable is some function of its previous values and some past random effects. These `autoregression` and `ARIMA` models capture serial correlation: the variable's correlation pattern with its prevous values. Using these correlation patterns to make short-term forecasts. Finally, the vector autoregression (VAR) exercise shows us how to use multiple variables for simultenous forecasting.

## This lecture

- feature engineering time series: trends and seasonal patterns 
- sample-splitting time series data
- cross-validation with time series
- the `fbprophet` library: modelling and cross-validation
- ARIMA models: specify lags for AR, I & MA manually and in auto mode
- handling trend and seasonality with ARIMA
- building VAR models
- forecasting and visualizing forecast uncertainty using fan charts

## Learning outcomes

After successfully completing the learning material, students will be familiar with

- understand the difference between deterministic and stoachastic time series and thier modelling
- feature engineering time series data
- forecasting using `fbprohet`
- how to define and test stochastic time series models